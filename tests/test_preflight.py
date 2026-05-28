import importlib.util
from pathlib import Path


def _load_preflight():
    p = Path(__file__).resolve().parents[1] / "ai" / "preflight.py"
    spec = importlib.util.spec_from_file_location("ai.preflight", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Preflight, mod.RiskLevel


def test_safe_command():
    Preflight, RiskLevel = _load_preflight()
    p = Preflight()
    assert p.score("echo hello") == RiskLevel.SAFE


def test_dangerous_patterns():
    Preflight, RiskLevel = _load_preflight()
    p = Preflight()
    cases = {
        "rm -rf /tmp": RiskLevel.IRREVERSIBLE,
        "git push --force origin main": RiskLevel.DESTRUCTIVE,
        "mkfs.ext4 /dev/sdb1": RiskLevel.IRREVERSIBLE,
        "chmod -R 777 somedir": RiskLevel.MUTATING,
        "dd if=/dev/zero of=/dev/sda bs=1M": RiskLevel.IRREVERSIBLE,
    }
    for cmd, expected in cases.items():
        assert p.score(cmd) == expected


def test_pattern_list_size():
    Preflight, _ = _load_preflight()
    p = Preflight()
    # Expect at least 25 heuristic rules to be present for Day 1
    assert len(p.PATTERNS) >= 25
