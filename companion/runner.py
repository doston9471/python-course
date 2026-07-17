"""Run lesson scripts and capture output."""

from __future__ import annotations

import shutil
import subprocess
import sys
from dataclasses import dataclass

from companion.lessons import Lesson, repo_root


@dataclass(frozen=True)
class RunResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def output(self) -> str:
        parts: list[str] = []
        if self.stdout:
            parts.append(self.stdout)
        if self.stderr:
            parts.append(self.stderr)
        text = "\n".join(parts).rstrip()
        if not text:
            text = "(no output)"
        return f"$ {' '.join(self.command)}\n\n{text}\n\n[exit {self.returncode}]"


def _build_command(lesson: Lesson) -> list[str]:
    if lesson.path.name == "08_testing_pytest.py":
        pytest_bin = shutil.which("pytest")
        if pytest_bin:
            return [pytest_bin, str(lesson.path), "-v"]
    return [sys.executable, str(lesson.path)]


def run_lesson(lesson: Lesson, timeout: float = 60.0) -> RunResult:
    command = _build_command(lesson)
    try:
        completed = subprocess.run(
            command,
            cwd=repo_root(),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return RunResult(
            command=command,
            returncode=completed.returncode,
            stdout=completed.stdout or "",
            stderr=completed.stderr or "",
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        return RunResult(
            command=command,
            returncode=124,
            stdout=stdout,
            stderr=(stderr + "\n[timed out]").lstrip(),
        )
    except OSError as exc:
        return RunResult(
            command=command,
            returncode=1,
            stdout="",
            stderr=f"Failed to run: {exc}",
        )
