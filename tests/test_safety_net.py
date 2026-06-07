import unittest
from types import SimpleNamespace
from unittest.mock import patch

from safety_net import Result, run
from ai.healer import HealingSuggestion


class SafetyNetTests(unittest.TestCase):
    def test_run_safe_command_capture(self):
        with patch("safety_net.validate_config", return_value=True), patch(
            "safety_net.show_preflight", return_value=SimpleNamespace(confirmed=True)
        ), patch(
            "safety_net._execute",
            return_value=Result(aborted=False, returncode=0, stdout="ok", stderr="", cmd="echo hi"),
        ):
            result = run("echo hi", mode="capture")
            self.assertFalse(result.aborted)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "ok")

    def test_healing_applies_suggested_fix(self):
        def fake_execute(cmd, mode):
            if cmd == "sudo mkdir /tmp/test-fix":
                return Result(aborted=False, returncode=0, stdout="created", stderr="", cmd=cmd)
            return Result(aborted=False, returncode=1, stdout="", stderr="permission denied", cmd=cmd)

        with patch("safety_net.validate_config", return_value=True), patch(
            "safety_net.show_preflight", return_value=SimpleNamespace(confirmed=True)
        ), patch("safety_net._execute", side_effect=fake_execute), patch(
            "safety_net.Healer.diagnose",
            return_value=HealingSuggestion(
                diagnosis="Permission denied.",
                suggested_command="sudo mkdir /tmp/test-fix",
                explanation="Run the command with elevated privileges.",
                confidence=0.8,
            ),
        ), patch("safety_net.show_healing", return_value=SimpleNamespace(confirmed=True)):
            result = run("mkdir /tmp/test-fail", mode="capture")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "created")

    def test_healing_skips_when_suggestion_declined(self):
        with patch("safety_net.validate_config", return_value=True), patch(
            "safety_net.show_preflight", return_value=SimpleNamespace(confirmed=True)
        ), patch(
            "safety_net._execute",
            return_value=Result(aborted=False, returncode=1, stdout="", stderr="permission denied", cmd="mkdir /tmp/test-fail"),
        ), patch(
            "safety_net.Healer.diagnose",
            return_value=HealingSuggestion(
                diagnosis="Permission denied.",
                suggested_command="sudo mkdir /tmp/test-fix",
                explanation="Run the command with elevated privileges.",
                confidence=0.8,
            ),
        ), patch("safety_net.show_healing", return_value=SimpleNamespace(confirmed=False)):
            result = run("mkdir /tmp/test-fail", mode="capture")
            self.assertEqual(result.returncode, 1)
