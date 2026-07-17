"""CLI course companion — browse, read, run, and track lessons."""

from __future__ import annotations

import sys

from companion.lessons import (
    Lesson,
    list_lessons,
    list_sections,
    section_label,
)
from companion.progress import Progress, load_progress, save_progress
from companion.runner import run_lesson


def _prompt(message: str = "> ") -> str:
    try:
        return input(message).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return "q"


def _pause() -> None:
    _prompt("Press Enter to continue… ")


def _print_header(progress: Progress) -> None:
    done, total = progress.overall_counts()
    print()
    print("Python Course Companion (CLI)")
    print("=" * 34)
    print(f"Progress: {done}/{total} lessons")
    print()


def _lesson_line(progress: Progress, lesson: Lesson, index: int) -> str:
    mark = "x" if progress.is_done(lesson) else " "
    num = f"{lesson.number} " if lesson.number else ""
    return f"  {index}) [{mark}] {num}{lesson.title}"


def _show_source(lesson: Lesson) -> None:
    print()
    print(f"--- {lesson.rel_path} ---")
    try:
        print(lesson.path.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"(could not read file: {exc})")
    print("--- end ---")
    print()


def _lesson_menu(progress: Progress, lesson: Lesson) -> Progress:
    while True:
        mark = "complete" if progress.is_done(lesson) else "incomplete"
        print()
        print(f"Lesson: {lesson.rel_path} ({mark})")
        print("  1) Show source")
        print("  2) Run")
        print("  3) Mark complete")
        print("  4) Mark incomplete")
        print("  0) Back")
        choice = _prompt()
        if choice in {"0", "b", "q"}:
            return progress
        if choice == "1":
            _show_source(lesson)
            _pause()
        elif choice == "2":
            print()
            result = run_lesson(lesson, stream=True)
            progress.last = lesson.rel_path
            save_progress(progress)
            print(f"Finished with exit {result.returncode}.")
            mark_now = _prompt("Mark complete? [y/N] ").lower()
            if mark_now in {"y", "yes"}:
                progress.mark_done(lesson)
                save_progress(progress)
                print("Marked complete.")
            else:
                save_progress(progress)
            _pause()
        elif choice == "3":
            progress.mark_done(lesson)
            save_progress(progress)
            print("Marked complete.")
        elif choice == "4":
            progress.mark_undone(lesson)
            save_progress(progress)
            print("Marked incomplete.")
        else:
            print("Unknown option.")


def _section_menu(progress: Progress, section: str) -> Progress:
    while True:
        lessons = list_lessons(section)
        done, total = progress.section_counts(section)
        print()
        print(f"{section_label(section)}  ({done}/{total})")
        for i, lesson in enumerate(lessons, start=1):
            print(_lesson_line(progress, lesson, i))
        print("  0) Back")
        choice = _prompt()
        if choice in {"0", "b", "q"}:
            return progress
        if not choice.isdigit():
            print("Enter a number.")
            continue
        index = int(choice)
        if index < 1 or index > len(lessons):
            print("Out of range.")
            continue
        progress = _lesson_menu(progress, lessons[index - 1])


def _continue_next(progress: Progress) -> Progress:
    nxt = progress.next_incomplete()
    if nxt is None:
        print("Every lesson is marked complete.")
        _pause()
        return progress
    print(f"Next: {nxt.rel_path}")
    return _lesson_menu(progress, nxt)


def main() -> None:
    progress = load_progress()
    sections = list_sections()
    if not sections:
        print("No course sections found.", file=sys.stderr)
        raise SystemExit(1)

    while True:
        _print_header(progress)
        for i, section in enumerate(sections, start=1):
            done, total = progress.section_counts(section)
            print(f"  {i}) {section_label(section)}  ({done}/{total})")
        print(f"  {len(sections) + 1}) Continue next lesson")
        print("  0) Quit")
        choice = _prompt()
        if choice in {"0", "q"}:
            print("Bye.")
            return
        if not choice.isdigit():
            print("Enter a number.")
            continue
        index = int(choice)
        if index == len(sections) + 1:
            progress = _continue_next(progress)
        elif 1 <= index <= len(sections):
            progress = _section_menu(progress, sections[index - 1])
        else:
            print("Out of range.")


if __name__ == "__main__":
    main()
