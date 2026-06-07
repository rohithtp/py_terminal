"""Prompt templates for AI preflight and healing assistance."""

from __future__ import annotations

from typing import List, Dict


PREFLIGHT_SYSTEM = (
    "You are a safety-focused terminal assistant. "
    "Analyze the provided shell command and explain any risks clearly and concisely. "
    "Only return valid JSON in the exact schema requested."
)

PREFLIGHT_USER = (
    "Analyze this shell command and return a JSON object with exactly three keys: "
    "plain_english_summary, affected_resources, reversibility_note. "
    "Do not add any commentary outside the JSON object."
)

HEALER_SYSTEM = (
    "You are a terminal repair assistant. "
    "Given a failed shell command and its failure artifacts, provide a short diagnosis and a safe suggested fix. "
    "Return only valid JSON in the exact schema requested."
)

HEALER_USER = (
    "A shell command failed. Analyze the failure and return a JSON object with the following keys: "
    "diagnosis, suggested_command, explanation, confidence. "
    "If you cannot suggest a safe automated fix, set suggested_command to null. "
    "Confidence should be a number between 0.0 and 1.0. "
    "Do not include any text outside the JSON object."
)


def preflight_messages(command: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": PREFLIGHT_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Command: {command}\n"
                "Return JSON with:"
                " {\"plain_english_summary\": string, "
                "\"affected_resources\": string, "
                "\"reversibility_note\": string }"
            ),
        },
    ]


def healing_messages(command: str, stderr: str, returncode: int, cwd: str, os_name: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": HEALER_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Command: {command}\n"
                f"Return code: {returncode}\n"
                f"Working directory: {cwd}\n"
                f"OS: {os_name}\n"
                f"Stderr: {stderr}\n"
                "Return JSON with:"
                " {\"diagnosis\": string, "
                "\"suggested_command\": string | null, "
                "\"explanation\": string, "
                "\"confidence\": number }"
            ),
        },
    ]
