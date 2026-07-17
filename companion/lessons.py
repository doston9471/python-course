"""Discover course sections and lesson files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

SECTION_DIRS = (
    "01_basics",
    "02_oop_and_solid",
    "03_advanced",
)

SECTION_LABELS = {
    "01_basics": "Basics",
    "02_oop_and_solid": "OOP & SOLID",
    "03_advanced": "Advanced",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Lesson:
    section: str
    path: Path  # absolute
    rel_path: str  # e.g. 01_basics/01_hello_and_print.py

    @property
    def title(self) -> str:
        stem = self.path.stem  # 01_hello_and_print
        parts = stem.split("_", 1)
        name = parts[1] if len(parts) == 2 else stem
        return name.replace("_", " ")

    @property
    def number(self) -> str:
        stem = self.path.stem
        prefix = stem.split("_", 1)[0]
        return prefix if prefix.isdigit() else ""


def list_sections() -> list[str]:
    root = repo_root()
    return [name for name in SECTION_DIRS if (root / name).is_dir()]


def section_label(section: str) -> str:
    return SECTION_LABELS.get(section, section)


def list_lessons(section: str) -> list[Lesson]:
    root = repo_root()
    folder = root / section
    if not folder.is_dir():
        return []
    lessons: list[Lesson] = []
    for path in sorted(folder.glob("*.py")):
        rel = f"{section}/{path.name}"
        lessons.append(Lesson(section=section, path=path, rel_path=rel))
    return lessons


def all_lessons() -> list[Lesson]:
    result: list[Lesson] = []
    for section in list_sections():
        result.extend(list_lessons(section))
    return result


def find_lesson(rel_path: str) -> Lesson | None:
    for lesson in all_lessons():
        if lesson.rel_path == rel_path:
            return lesson
    return None
