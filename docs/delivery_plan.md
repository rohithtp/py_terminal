# Delivery & Implementation Plan

This document outlines a pragmatic, step-by-step plan to deliver `py_terminal` to general users and developers. It is intended as a living checklist to guide implementation, CI, and release tasks.

## Objectives

- Provide a reproducible, easy-to-run distribution for non-developers (primary: Docker image).
- Keep a simple developer install path (`pip` / virtualenv) for contributors.
- Offer optional native binaries for end-users who prefer no Docker or Python installs.
- Preserve safety and privacy (safety preflight, explicit API-key handling, opt-out mode).

## Deliverables

- `docs/` updates and Quickstart snippets
- `Dockerfile` and `docker/` example configuration
- `.env.example` documenting env vars (API keys, provider selection)
- `pyproject.toml` / `setup.cfg` for pip packaging and `console_scripts` entry
- CI workflows: tests, image build & publish, release artifacts
- Optional: `dist/` PyInstaller specs + built binaries attached to GitHub Releases

## Implementation Steps

1. Docs & Quickstart
   - Add `docs/delivery_plan.md` (this file).
   - Update `README.md` with a `Quickstart` section: Docker and pip snippets.
   - Add `.env.example` with `OPENAI_API_KEY`, `LLM_PROVIDER`, `LLM_MODEL`, `LITELLM_*` placeholders.

2. Docker Support (primary)
   - Create `Dockerfile` (minimal, slim Python base) to install `requirements.txt` and run `python terminal_web/main.py`.
   - Document `docker build` and `docker run` examples including `-it` and `-e` for API keys.
   - Add `docker/README.md` with recommended runtime flags (TTY, security notes, mounting workspace if desired).

3. Developer Install (secondary)
   - Add `pyproject.toml` with metadata and a `console_scripts` entrypoint (e.g., `py-terminal = terminal_web.main:main`).
   - Ensure `requirements.txt` stays in sync with `pyproject.toml` or use `pip-tools` to lock dev deps.

4. Safe Defaults & No-API Fallback
   - Implement a runtime fallback that disables LLM features when no API key is present and clearly notifies the user.
   - Ensure `safety_net` defaults to conservative behavior; require confirmation for MUTATING commands.

5. Native Binaries (optional)
   - Add a `packaging/pyinstaller.spec` and a small CI job to build Linux and macOS binaries (where supported).
   - Test binaries for networking and runtime configuration behavior.

6. CI / Releases
   - GitHub Actions jobs:
     - `test`: run Python unit tests under `tests/` on multiple Python versions.
     - `lint`: optional, run `ruff`/`black` or similar.
     - `build-image`: build Docker image and push to GHCR on tags/releases.
     - `release`: build PyPI artifact and attach PyInstaller binaries to GitHub Releases (optional).

7. Demo & Submission Assets
   - Create a short GIF showing the TUI and the `Show Status` workflow.
   - Add a short `docs/DEMO.md` with sample commands and expected outputs.

## Timeline & Acceptance Criteria (suggested)

- Day 1: Add `Dockerfile`, `.env.example`, README quickstart, and `docs/` plan (acceptance: Docker image runs interactively with `-it` and disables LLM without API key).
- Day 2: Add `pyproject.toml` with `console_scripts`, CI skeleton, and unit test run (acceptance: `pip install -e .` provides `py-terminal` CLI and tests pass).
- Day 3: Add Docker publish workflow, demo GIF, and submission assets (acceptance: Docker image built by CI on tag and demo included).

## Security & Privacy Notes

- Never embed API keys in code or images. Pass keys through env vars or secret stores.
- Document exactly what is sent to LLM providers and provide a local/no-API mode.
- Consider a telemetry opt-in if you collect usage data (document and provide opt-out).

## Next Steps (pick one)

- Implement `Dockerfile` + README examples (recommended first action).
- Or scaffold `pyproject.toml` + `console_scripts` for `pip` distribution.

---

Keep this plan updated as choices are implemented and tests pass.
