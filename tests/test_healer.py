from ai.healer import Healer


def test_healer_offline_permission_denied():
    healer = Healer(use_llm=False)
    suggestion = healer.diagnose(
        "cat /etc/shadow",
        {"stderr": "cat: /etc/shadow: Permission denied", "returncode": 1},
    )

    assert suggestion.diagnosis.startswith("Permission denied")
    assert suggestion.suggested_command == "sudo cat /etc/shadow"
    assert suggestion.confidence > 0.5


def test_healer_offline_command_not_found():
    healer = Healer(use_llm=False)
    suggestion = healer.diagnose(
        "foobarbaz",
        {"stderr": "sh: 1: foobarbaz: not found", "returncode": 127},
    )

    assert suggestion.diagnosis.startswith("The command or executable was not found")
    assert suggestion.suggested_command is None
    assert suggestion.confidence < 0.4
