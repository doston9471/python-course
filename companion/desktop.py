"""Tkinter desktop course companion."""

from __future__ import annotations

import sys

try:
    import tkinter as tk
    from tkinter import messagebox, ttk
except ModuleNotFoundError as exc:  # pragma: no cover - env-specific
    print(
        "Tkinter is not available for this Python.\n\n"
        "Homebrew Python often needs:\n"
        "  brew install python-tk@3.14\n\n"
        "Or run with macOS system Python:\n"
        "  /usr/bin/python3 -m companion\n",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

from companion.lessons import (
    Lesson,
    list_lessons,
    list_sections,
    section_label,
)
from companion.progress import Progress, load_progress, save_progress
from companion.runner import run_lesson


class CourseCompanionApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Python Course Companion")
        self.geometry("1100x720")
        self.minsize(800, 520)

        self.progress: Progress = load_progress()
        self.sections = list_sections()
        self.current_section: str | None = None
        self.lessons: list[Lesson] = []
        self.selected_lesson: Lesson | None = None

        self._build_ui()
        if self.sections:
            self.section_list.selection_set(0)
            self._on_section_select()
        self._refresh_header()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, padding=(12, 10, 12, 6))
        header.grid(row=0, column=0, sticky="ew")
        self.header_var = tk.StringVar(value="Progress: 0/0")
        ttk.Label(header, textvariable=self.header_var, font=("", 14, "bold")).pack(
            side="left"
        )
        ttk.Button(header, text="Continue next", command=self._continue_next).pack(
            side="right"
        )

        body = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        body.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 8))

        left = ttk.Frame(body, padding=4)
        center = ttk.Frame(body, padding=4)
        right = ttk.Frame(body, padding=4)
        body.add(left, weight=1)
        body.add(center, weight=2)
        body.add(right, weight=3)

        ttk.Label(left, text="Sections").pack(anchor="w")
        self.section_list = tk.Listbox(left, exportselection=False, height=16)
        self.section_list.pack(fill="both", expand=True)
        self.section_list.bind("<<ListboxSelect>>", lambda _e: self._on_section_select())
        for section in self.sections:
            self.section_list.insert(tk.END, self._section_row_text(section))

        ttk.Label(center, text="Lessons").pack(anchor="w")
        self.lesson_list = tk.Listbox(center, exportselection=False, height=16)
        self.lesson_list.pack(fill="both", expand=True)
        self.lesson_list.bind("<<ListboxSelect>>", lambda _e: self._on_lesson_select())

        actions = ttk.Frame(center)
        actions.pack(fill="x", pady=(8, 0))
        ttk.Button(actions, text="Run", command=self._run_selected).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(actions, text="Mark complete", command=self._mark_complete).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(actions, text="Mark incomplete", command=self._mark_incomplete).pack(
            side="left"
        )

        self.tabs = ttk.Notebook(right)
        self.tabs.pack(fill="both", expand=True)

        source_frame = ttk.Frame(self.tabs, padding=2)
        output_frame = ttk.Frame(self.tabs, padding=2)
        self.tabs.add(source_frame, text="Lesson")
        self.tabs.add(output_frame, text="Output")

        source_frame.rowconfigure(0, weight=1)
        source_frame.columnconfigure(0, weight=1)
        self.source = tk.Text(source_frame, wrap="none", height=20, undo=False)
        source_scroll_y = ttk.Scrollbar(
            source_frame, orient="vertical", command=self.source.yview
        )
        source_scroll_x = ttk.Scrollbar(
            source_frame, orient="horizontal", command=self.source.xview
        )
        self.source.configure(
            yscrollcommand=source_scroll_y.set,
            xscrollcommand=source_scroll_x.set,
            font=("Menlo", 12),
            state="disabled",
        )
        self.source.grid(row=0, column=0, sticky="nsew")
        source_scroll_y.grid(row=0, column=1, sticky="ns")
        source_scroll_x.grid(row=1, column=0, sticky="ew")

        output_frame.rowconfigure(0, weight=1)
        output_frame.columnconfigure(0, weight=1)
        self.output = tk.Text(output_frame, wrap="word", height=20, undo=False)
        output_scroll = ttk.Scrollbar(
            output_frame, orient="vertical", command=self.output.yview
        )
        self.output.configure(
            yscrollcommand=output_scroll.set,
            font=("Menlo", 12),
            state="disabled",
        )
        self.output.grid(row=0, column=0, sticky="nsew")
        output_scroll.grid(row=0, column=1, sticky="ns")

        footer = ttk.Frame(self, padding=(12, 0, 12, 10))
        footer.grid(row=2, column=0, sticky="ew")
        self.status_var = tk.StringVar(
            value="Select a lesson to read it, then Run. Interactive input() lessons work best in a terminal."
        )
        ttk.Label(footer, textvariable=self.status_var, wraplength=1000).pack(anchor="w")

    def _section_row_text(self, section: str) -> str:
        done, total = self.progress.section_counts(section)
        return f"{section_label(section)}  ({done}/{total})"

    def _lesson_row_text(self, lesson: Lesson) -> str:
        mark = "x" if self.progress.is_done(lesson) else " "
        num = f"{lesson.number}  " if lesson.number else ""
        return f"[{mark}] {num}{lesson.title}"

    def _refresh_header(self) -> None:
        done, total = self.progress.overall_counts()
        self.header_var.set(f"Progress: {done}/{total} lessons")

    def _refresh_sections(self) -> None:
        selected = self.section_list.curselection()
        self.section_list.delete(0, tk.END)
        for section in self.sections:
            self.section_list.insert(tk.END, self._section_row_text(section))
        if selected:
            self.section_list.selection_set(selected[0])

    def _refresh_lessons(self, select_rel: str | None = None) -> None:
        self.lesson_list.delete(0, tk.END)
        select_index = 0
        for i, lesson in enumerate(self.lessons):
            self.lesson_list.insert(tk.END, self._lesson_row_text(lesson))
            if select_rel and lesson.rel_path == select_rel:
                select_index = i
        if self.lessons:
            self.lesson_list.selection_clear(0, tk.END)
            self.lesson_list.selection_set(select_index)
            self.lesson_list.see(select_index)
            self.selected_lesson = self.lessons[select_index]
            self._show_lesson_source(self.selected_lesson)
        else:
            self.selected_lesson = None
            self._set_text(self.source, "")

    def _on_section_select(self) -> None:
        idxs = self.section_list.curselection()
        if not idxs:
            return
        section = self.sections[idxs[0]]
        self.current_section = section
        self.lessons = list_lessons(section)
        self._refresh_lessons()
        self.status_var.set(f"Section: {section_label(section)}")

    def _on_lesson_select(self) -> None:
        idxs = self.lesson_list.curselection()
        if not idxs:
            return
        self.selected_lesson = self.lessons[idxs[0]]
        self._show_lesson_source(self.selected_lesson)
        self.status_var.set(self.selected_lesson.rel_path)

    def _set_text(self, widget: tk.Text, text: str) -> None:
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, text)
        widget.configure(state="disabled")

    def _show_lesson_source(self, lesson: Lesson) -> None:
        try:
            content = lesson.path.read_text(encoding="utf-8")
        except OSError as exc:
            content = f"# Could not read {lesson.rel_path}\n# {exc}\n"
        self._set_text(self.source, content)
        self.tabs.select(0)

    def _set_output(self, text: str) -> None:
        self._set_text(self.output, text)
        self.tabs.select(1)

    def _run_selected(self) -> None:
        if not self.selected_lesson:
            messagebox.showinfo("No lesson", "Select a lesson first.")
            return
        lesson = self.selected_lesson
        self.status_var.set(f"Running {lesson.rel_path}…")
        self.update_idletasks()
        result = run_lesson(lesson)
        self._set_output(result.output)
        self.progress.last = lesson.rel_path
        save_progress(self.progress)
        self.status_var.set(
            f"Finished {lesson.rel_path} (exit {result.returncode}). "
            "Use Mark complete when you are done with this lesson."
        )

    def _mark_complete(self) -> None:
        if not self.selected_lesson:
            messagebox.showinfo("No lesson", "Select a lesson first.")
            return
        lesson = self.selected_lesson
        self.progress.mark_done(lesson)
        save_progress(self.progress)
        self._refresh_header()
        self._refresh_sections()
        self._refresh_lessons(select_rel=lesson.rel_path)
        self.status_var.set(f"Marked complete: {lesson.rel_path}")

    def _mark_incomplete(self) -> None:
        if not self.selected_lesson:
            messagebox.showinfo("No lesson", "Select a lesson first.")
            return
        lesson = self.selected_lesson
        self.progress.mark_undone(lesson)
        save_progress(self.progress)
        self._refresh_header()
        self._refresh_sections()
        self._refresh_lessons(select_rel=lesson.rel_path)
        self.status_var.set(f"Marked incomplete: {lesson.rel_path}")

    def _continue_next(self) -> None:
        nxt = self.progress.next_incomplete()
        if nxt is None:
            messagebox.showinfo("All done", "Every lesson is marked complete.")
            return
        if nxt.section in self.sections:
            idx = self.sections.index(nxt.section)
            self.section_list.selection_clear(0, tk.END)
            self.section_list.selection_set(idx)
            self.section_list.see(idx)
        self.current_section = nxt.section
        self.lessons = list_lessons(nxt.section)
        self._refresh_lessons(select_rel=nxt.rel_path)
        self.selected_lesson = nxt
        self._run_selected()


def main() -> None:
    app = CourseCompanionApp()
    app.mainloop()


if __name__ == "__main__":
    main()
