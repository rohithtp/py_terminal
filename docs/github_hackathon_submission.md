*This is a submission for the [GitHub Finish-Up-A-Thon Challenge](https://dev.to/challenges/github-2026-05-21)*

## What I Built
**Terminal Web (`py_terminal`)** is a powerful terminal-based UI web project utilizing Python and the [Rich](https://github.com/Textualize/rich) library for beautiful terminal output combined with advanced command execution capabilities.

As part of the Finish-Up-A-Thon, I transformed this tool by integrating an **AI Safety Net**—a proactive layer designed to protect users from executing destructive shell commands (e.g., `rm -rf`, `git push --force`) while maintaining a fluid and rapid developer experience. The safety net employs:
- **Tier-1 Heuristics:** Instant, offline protection against common dangerous commands.
- **Tier-2 AI Preflight:** LLM-powered risk analysis that summarizes potential consequences and affected resources for `MUTATING+` risk levels.
- **Intelligent Self-Healing:** A workflow that diagnoses failed commands (e.g., permission errors, missing paths) and suggests safe alternatives to get you back on track.

## Demo
**Project Repository:** [https://github.com/rohithtp/py_terminal](https://github.com/rohithtp/py_terminal)

<!-- Add your video walkthrough or screenshots below this line -->
*(Insert a screenshot of the Preflight Warning Panel or Healing Suggestion Panel here!)*

## The Comeback Story
Previously, `py_terminal` was an effective CLI wrapper with dual execution modes (interactive and capture) and beautifully formatted outputs. However, it had one critical flaw: it blindly executed whatever bash command was provided, offering no protection against accidental system damage. In a modern development environment where LLMs are sometimes used to generate complex, unverified commands, ensuring those commands are safe to run locally became a high priority.

To "finish it up" for this hackathon, I drastically leveled up the tool's intelligence and safety by adding:
- **An AI Preflight Loop:** Intercepts risky commands, uses LLMs to generate reversibility notes, and blocks execution until explicit user confirmation is given.
- **A Self-Healing Workflow:** Catches non-zero exit codes, diagnoses the error (e.g., "No such file or directory"), and proposes an LLM-generated fix that gets re-routed through the safety preflight loop.
- **SQLite Caching:** Caches preflight AI evaluations to avoid duplicate API calls and guarantees zero latency for repeated commands.
- **Offline Graceful Degradation:** The UI falls back beautifully to local heuristic warnings when the LLM API is unavailable, ensuring the tool is always usable.
- **A Status Capture Utility:** A built-in telemetry tool to rapidly verify repository and dependency health.

## My Experience with GitHub Copilot
GitHub Copilot acted as an exceptionally fast pair programmer throughout this challenge. It was instrumental in scaffolding the `pexpect`-based automated test suite for validating the AI Safety Net, mocking out LLM network responses, and quickly laying out the boilerplate for the Rich UI panels. 

When constructing the SQLite caching mechanism, Copilot seamlessly anticipated the database schema I needed and handled boilerplate queries, allowing me to focus entirely on the core business logic of the safety heuristics and healing loop. It transformed complex refactoring and UI layout tasks into smooth, effortless completions.

---
**Team Members:** @rohithtp
