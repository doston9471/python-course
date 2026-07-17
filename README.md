# Python Course — From Zero to Advanced

A hands-on, step-by-step Python course with runnable lessons.

## Prerequisites

Python 3.10+ recommended (tested with 3.14).

```bash
python3 --version
```

### Version manager (like rbenv for Ruby)

Use **[pyenv](https://github.com/pyenv/pyenv)**:

```bash
brew install pyenv
pyenv install 3.14.6
pyenv global 3.14.6
```

Other options: **asdf** (multi-language), **uv** (fast installs + venvs).

## Course structure

- `01_basics` — Python syntax and foundations
- `02_oop_and_solid` — OOP + SOLID principles
- `03_advanced` — post-OOP advanced topics

## Course companion

Browse sections, read lessons, run them, and track progress. Progress is saved in `progress.json` (gitignored).

### CLI (works with any Python 3.10+)

```bash
python3 course_runner.py
# or
python3 -m companion.cli
```

### Desktop (Tkinter)

```bash
python3 -m companion
# or
python3 -m companion.desktop
```

If the desktop app fails with `No module named '_tkinter'`:

```bash
# Option A — macOS system Python
/usr/bin/python3 -m companion

# Option B — Homebrew Tk for your Python version
brew install python-tk@3.14
```

## How to run lessons

```bash
# Via the companion (recommended)
python3 course_runner.py
python3 -m companion

# Or run a lesson file directly
python3 01_basics/01_hello_and_print.py
python3 02_oop_and_solid/01_classes_and_objects.py
python3 03_advanced/01_type_hints.py
```

## Part 1 — Basics

See [`01_basics/README.md`](./01_basics/README.md).

## Part 2 — OOP + SOLID

See [`02_oop_and_solid/README.md`](./02_oop_and_solid/README.md).

## Part 3 — Advanced

See [`03_advanced/README.md`](./03_advanced/README.md).

## Suggested learning path

1. Complete `01_basics`
2. Complete OOP in `02_oop_and_solid` (01–12)
3. Complete SOLID in `02_oop_and_solid` (13–18)
4. Continue with `03_advanced`

## License

This project is licensed under the MIT License — see [LICENSE](./LICENSE).
