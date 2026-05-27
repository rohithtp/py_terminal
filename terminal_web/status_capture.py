"""Status Capture utility for workspace auditing and environment reporting.

This module provides a small, modular tool to inspect a repository workspace
and produce a unified status summary including workspace file checks,
git metadata, system environment info, and dependency health.

Usage:
    python -m terminal_web.status_capture        # prints pretty report
    python -m terminal_web.status_capture --json # prints JSON

Functions:
    gather_status(path=".") -> dict
    print_status(status: dict) -> None

The code uses only the Python standard library (3.8+) and handles missing
files or absent git gracefully.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    # Python 3.8+: importlib.metadata is in stdlib; for older Pythons, it's optional
    from importlib import metadata as importlib_metadata
except Exception:
    import importlib_metadata  # type: ignore


@dataclass
class FileCheck:
    path: str
    exists: bool
    is_dir: bool
    size: Optional[int]
    mtime: Optional[str]


def _fmt_ts(ts: Optional[float]) -> Optional[str]:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts).isoformat()


def _check_file(base: Path, rel: str) -> FileCheck:
    p = base.joinpath(rel)
    exists = p.exists()
    is_dir = p.is_dir()
    size = None
    mtime = None
    try:
        if exists and p.is_file():
            size = p.stat().st_size
            mtime = _fmt_ts(p.stat().st_mtime)
    except Exception:
        pass
    return FileCheck(path=str(rel), exists=exists, is_dir=is_dir, size=size, mtime=mtime)


def _run_git(base: Path) -> Dict[str, Optional[str]]:
    git_dir = base.joinpath('.git')
    if not git_dir.exists():
        return {"git_available": False}

    def _call(args: List[str]) -> Tuple[bool, str]:
        try:
            out = subprocess.check_output(args, cwd=str(base), stderr=subprocess.DEVNULL)
            return True, out.decode().strip()
        except Exception:
            return False, ""

    ok, commit = _call([shutil.which('git') or 'git', 'rev-parse', 'HEAD'])
    ok_short, short = _call([shutil.which('git') or 'git', 'rev-parse', '--short', 'HEAD'])
    ok_meta, meta = _call([shutil.which('git') or 'git', 'log', '-1', '--pretty=format:%H|%an|%aI'])
    if ok_meta and '|' in meta:
        h, author, authored_iso = meta.split('|', 2)
    else:
        h = commit if ok else None
        author = None
        authored_iso = None

    return {
        "git_available": True,
        "commit": h,
        "commit_short": short if ok_short else None,
        "author": author,
        "authored_iso": authored_iso,
    }


def _parse_requirements(requirements_text: str) -> List[str]:
    pkgs: List[str] = []
    for raw in requirements_text.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        # Remove inline comments
        if ' #' in line:
            line = line.split(' #', 1)[0].strip()
        # Remove editable installs and VCS refs
        if line.startswith('-e') or line.startswith('git+') or '://' in line:
            continue
        # Strip version specifiers and extras, like pkg[extra]>=1.2
        name = re.split(r"[<>=!~]", line, 1)[0].strip()
        name = re.split(r"\[", name, 1)[0].strip()
        if name:
            pkgs.append(name)
    return pkgs


def _check_dependencies(base: Path) -> Dict[str, Dict[str, Optional[str]]]:
    req_file = base.joinpath('requirements.txt')
    deps: Dict[str, Dict[str, Optional[str]]] = {}
    if not req_file.exists():
        return {
            "declared_requirements_file": False,
            "packages": deps,
        }

    try:
        text = req_file.read_text(encoding='utf-8')
    except Exception:
        return {"declared_requirements_file": True, "packages": deps}

    pkgs = _parse_requirements(text)
    for name in pkgs:
        try:
            ver = importlib_metadata.version(name)
            deps[name] = {"installed": True, "version": ver}
        except importlib_metadata.PackageNotFoundError:
            deps[name] = {"installed": False, "version": None}
        except Exception:
            deps[name] = {"installed": None, "version": None}

    return {"declared_requirements_file": True, "packages": deps}


def gather_status(path: str = '.') -> Dict:
    """Gather a structured status summary for the workspace at `path`.

    Returns a dictionary containing:
      - workspace: file checks
      - git: git metadata (if available)
      - system: OS and Python info
      - dependencies: requirement checks
      - generated_at: timestamp
    """
    base = Path(path).resolve()
    now = datetime.utcnow().isoformat() + 'Z'

    key_files = [
        'README.md',
        'LICENSE',
        'pyproject.toml',
        'setup.py',
        'requirements.txt',
        '.git',
        'terminal_web',
        'info.md',
    ]

    files = [_check_file(base, f) for f in key_files]

    git = _run_git(base)

    # System/environment
    system = {
        "platform": sys.platform,
        "platform_details": os.name,
        "python_version": sys.version.splitlines()[0],
        "executable": sys.executable,
    }

    # pip version (best-effort)
    try:
        pip_ver = importlib_metadata.version('pip')
    except Exception:
        pip_ver = None
    system["pip_version"] = pip_ver

    deps = _check_dependencies(base)

    return {
        "generated_at": now,
        "workspace_path": str(base),
        "workspace_checks": [asdict(f) for f in files],
        "git": git,
        "system": system,
        "dependencies": deps,
    }


def print_status(status: Dict, json_out: bool = False) -> None:
    """Print the status to the terminal; optionally output JSON."""
    if json_out:
        print(json.dumps(status, indent=2))
        return

    # Pretty print
    print('--- Status Capture Report ---')
    print(f"Generated: {status.get('generated_at')}")
    print(f"Workspace: {status.get('workspace_path')}")
    print('\nWorkspace checks:')
    for f in status.get('workspace_checks', []):
        ok = 'DIR' if f.get('is_dir') else ('FILE' if f.get('exists') else 'MISSING')
        size = f.get('size')
        mtime = f.get('mtime')
        print(f" - {f.get('path')}: {ok}" + (f" (size={size} bytes)" if size else '') + (f" modified={mtime}" if mtime else ''))

    print('\nGit:')
    git = status.get('git', {})
    if not git.get('git_available'):
        print(' - Git: not available or not a git repository')
    else:
        print(f" - commit: {git.get('commit_short') or git.get('commit')}")
        if git.get('author'):
            print(f" - author: {git.get('author')}")
        if git.get('authored_iso'):
            print(f" - authored: {git.get('authored_iso')}")

    print('\nSystem:')
    sysinfo = status.get('system', {})
    print(f" - platform: {sysinfo.get('platform')} ({sysinfo.get('platform_details')})")
    print(f" - python: {sysinfo.get('python_version')}")
    print(f" - pip: {sysinfo.get('pip_version')}")

    print('\nDependencies (from requirements.txt):')
    deps = status.get('dependencies', {})
    if not deps.get('declared_requirements_file'):
        print(' - No requirements.txt found')
    else:
        packages = deps.get('packages', {})
        if not packages:
            print(' - requirements.txt present but no parseable packages')
        else:
            for name, info in packages.items():
                inst = info.get('installed')
                ver = info.get('version')
                if inst is True:
                    print(f" - {name}: installed ({ver})")
                elif inst is False:
                    print(f" - {name}: MISSING")
                else:
                    print(f" - {name}: unknown")


def _main(argv: Optional[List[str]] = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description='Status Capture utility')
    parser.add_argument('--path', '-p', default='.', help='Workspace path to inspect')
    parser.add_argument('--json', action='store_true', help='Output JSON instead of pretty text')
    parser.add_argument('--output', '-o', help='Write JSON output to file')
    args = parser.parse_args(argv)

    status = gather_status(args.path)
    if args.output:
        try:
            Path(args.output).write_text(json.dumps(status, indent=2), encoding='utf-8')
            print(f"Wrote status JSON to {args.output}")
        except Exception as e:
            print(f"Failed to write output: {e}", file=sys.stderr)
            return 2

    print_status(status, json_out=args.json)
    return 0


if __name__ == '__main__':
    raise SystemExit(_main())
