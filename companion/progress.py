"""Load and save course progress."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from companion.lessons import Lesson, all_lessons, repo_root


def progress_path() -> Path:
    return repo_root() / "progress.json"


@dataclass
class Progress:
    completed: list[str] = field(default_factory=list)
    last: str | None = None

    def is_done(self, lesson: Lesson) -> bool:
        return lesson.rel_path in self.completed

    def mark_done(self, lesson: Lesson) -> None:
        if lesson.rel_path not in self.completed:
            self.completed.append(lesson.rel_path)
        self.last = lesson.rel_path

    def mark_undone(self, lesson: Lesson) -> None:
        self.completed = [p for p in self.completed if p != lesson.rel_path]

    def section_counts(self, section: str) -> tuple[int, int]:
        lessons = [L for L in all_lessons() if L.section == section]
        done = sum(1 for L in lessons if self.is_done(L))
        return done, len(lessons)

    def overall_counts(self) -> tuple[int, int]:
        lessons = all_lessons()
        done = sum(1 for L in lessons if self.is_done(L))
        return done, len(lessons)

    def next_incomplete(self) -> Lesson | None:
        lessons = all_lessons()
        if not lessons:
            return None

        start_index = 0
        if self.last:
            for i, lesson in enumerate(lessons):
                if lesson.rel_path == self.last:
                    start_index = i + 1
                    break

        for lesson in lessons[start_index:] + lessons[:start_index]:
            if not self.is_done(lesson):
                return lesson
        return None


def load_progress() -> Progress:
    path = progress_path()
    if not path.is_file():
        return Progress()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return Progress()
    completed = data.get("completed") or []
    if not isinstance(completed, list):
        completed = []
    last = data.get("last")
    if last is not None and not isinstance(last, str):
        last = None
    return Progress(
        completed=[str(p) for p in completed],
        last=last,
    )


def save_progress(progress: Progress) -> None:
    path = progress_path()
    payload = {
        "completed": progress.completed,
        "last": progress.last,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
