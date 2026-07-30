# Container Vulnerability Report
**Image:** `python:3.12-alpine`

## Target: Python
| ID | Package | Severity | Status | Installed | Fixed | Title |
|---|---|---|---|---|---|---|
| CVE-2025-8869 | pip | MEDIUM | fixed | 25.0.1 | 25.3 | pip: pip missing checks on symbolic link extraction |
| CVE-2026-3219 | pip | MEDIUM | fixed | 25.0.1 | 26.1 | pip: pip: Incorrect file installation due to improper archive handling |
| CVE-2026-6357 | pip | MEDIUM | fixed | 25.0.1 | 26.1 | pip: pip: Arbitrary code execution or information disclosure via malicious wheel package installation |
| CVE-2026-8643 | pip | MEDIUM | fixed | 25.0.1 | 26.1.2 | python-pip: Path traversal via malicious entry point name in pip wheel installation allows arbitrary file overwrite |
| CVE-2026-1703 | pip | LOW | fixed | 25.0.1 | 26.0 | pip: pip: Information disclosure via path traversal when installing crafted wheel archives |
