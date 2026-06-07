import hashlib
import json
import os
import sqlite3
import time
from typing import Any, Optional

from ai.config import CACHE_DIR, CACHE_TTL_SECONDS, ENABLE_CACHE

DB_FILENAME = "cache.sqlite"
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS cache (
    key TEXT PRIMARY KEY,
    created_at REAL NOT NULL,
    value TEXT NOT NULL
)
"""


def _db_path() -> str:
    return os.path.join(CACHE_DIR, DB_FILENAME)


def _ensure_db() -> Optional[sqlite3.Connection]:
    if not ENABLE_CACHE:
        return None

    os.makedirs(CACHE_DIR, exist_ok=True)
    conn = sqlite3.connect(_db_path(), timeout=30)
    conn.execute(CREATE_TABLE_SQL)
    conn.commit()
    return conn


def _make_key(namespace: str, command: str, context: str = "") -> str:
    payload = f"{namespace}|{command}|{context}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def get_cached_response(namespace: str, command: str, context: str = "") -> Optional[Any]:
    conn = _ensure_db()
    if conn is None:
        return None

    try:
        key = _make_key(namespace, command, context)
        row = conn.execute(
            "SELECT created_at, value FROM cache WHERE key = ?",
            (key,),
        ).fetchone()
        if not row:
            return None

        created_at, value = row
        if time.time() - float(created_at) > CACHE_TTL_SECONDS:
            conn.execute("DELETE FROM cache WHERE key = ?", (key,))
            conn.commit()
            return None

        return json.loads(value)
    except Exception:
        return None
    finally:
        conn.close()


def set_cached_response(namespace: str, command: str, context: str, payload: Any) -> None:
    conn = _ensure_db()
    if conn is None:
        return

    try:
        key = _make_key(namespace, command, context)
        value = json.dumps(payload)
        conn.execute(
            "INSERT OR REPLACE INTO cache (key, created_at, value) VALUES (?, ?, ?)",
            (key, time.time(), value),
        )
        conn.commit()
    except Exception:
        pass
    finally:
        conn.close()
