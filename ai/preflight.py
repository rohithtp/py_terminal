import re
from enum import IntEnum


class RiskLevel(IntEnum):
    SAFE = 0
    MUTATING = 1
    DESTRUCTIVE = 2
    IRREVERSIBLE = 3


class Preflight:
    """Tier-1 heuristic preflight scanner."""

    # Simple pattern list mapping to risk level
    PATTERNS = [
        (r"\brm\s+-rf\b", RiskLevel.IRREVERSIBLE),
        (r"\brm\s+-r\b", RiskLevel.MUTATING),
        (r"\bdd\s+if=", RiskLevel.IRREVERSIBLE),
        (r"\bmkfs\b", RiskLevel.IRREVERSIBLE),
        (r"\bchmod\s+-R\b", RiskLevel.MUTATING),
        (r"git\s+push\s+--force", RiskLevel.DESTRUCTIVE),
        (r"git\s+reset\s+--hard", RiskLevel.DESTRUCTIVE),
        (r"\bDROP\s+TABLE\b", RiskLevel.IRREVERSIBLE),
        (r">\s*/dev/sd", RiskLevel.IRREVERSIBLE),
        (r"\bkubectl\s+delete\b", RiskLevel.DESTRUCTIVE),
        (r"\bterraform\s+destroy\b", RiskLevel.IRREVERSIBLE),
        (r":\(\)\s*\{\s*:\|:\s*&\s*\};", RiskLevel.IRREVERSIBLE),
        (r"\brm\s+-f\b", RiskLevel.MUTATING),
        (r"\bshutdown\b", RiskLevel.DESTRUCTIVE),
        (r"\breboot\b", RiskLevel.DESTRUCTIVE),
        (r"\bdd\b.*of=", RiskLevel.IRREVERSIBLE),
        (r"\bmkfs\.[a-z0-9]+\b", RiskLevel.IRREVERSIBLE),
        (r"\bscp\s+.*:~?/.+\s", RiskLevel.MUTATING),
        (r"\bchown\s+-R\b", RiskLevel.MUTATING),
        (r"\bfsck\b", RiskLevel.MUTATING),
        (r"\bformat\b", RiskLevel.IRREVERSIBLE),
        (r"\bdd\s+of=/dev/", RiskLevel.IRREVERSIBLE),
        (r"\bshutdown\s+-h\b", RiskLevel.DESTRUCTIVE),
        (r"\biptables\s+-F\b", RiskLevel.DESTRUCTIVE),
        (r"\b>\s+/dev/null\s+2>&1\s*;\s*rm\b", RiskLevel.IRREVERSIBLE),
        (r"\bgit\s+branch\s+-D\b", RiskLevel.DESTRUCTIVE),
        (r"\btruncate\b", RiskLevel.MUTATING),
        (r"\b:>\b", RiskLevel.MUTATING),
        (r"\becho\s+''\s*>\s+", RiskLevel.MUTATING),
    ]

    def __init__(self):
        # compile regexes
        self._compiled = [(re.compile(p, re.IGNORECASE), lvl) for p, lvl in self.PATTERNS]

    def score(self, cmd: str):
        """Return the highest RiskLevel matched for a command string."""
        if not cmd:
            return RiskLevel.SAFE
        level = RiskLevel.SAFE
        for regex, lvl in self._compiled:
            if regex.search(cmd):
                if lvl > level:
                    level = lvl
        return level


__all__ = ["Preflight", "RiskLevel"]
