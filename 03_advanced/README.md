# Python Advanced — After OOP

Topics that are easier once you know basics + OOP. Each lesson is a runnable `.py` file.

## Suggested order

1. Finish `01_basics/`
2. Finish OOP + SOLID lessons in `02_oop_and_solid/` (`01`–`18`)
3. Come here

## How to run

```bash
python3 03_advanced/01_type_hints.py
python3 03_advanced/05_async_await.py

# testing lesson (after installing pytest in a venv)
pytest 03_advanced/08_testing_pytest.py -v
```

## Curriculum

1. Type hints — annotate functions & classes (`list[int]`, `| None`)
2. Generators — `yield`, generator expressions, pipelines
3. Decorators — wrap functions, `@wraps`, decorators with args
4. Tooling — venv, pip, uv, `requirements.txt`
5. Async / await — `asyncio`, gather, concurrent I/O
6. Regex — `re` search, groups, sub, compile
7. Dataclasses — `@dataclass`, frozen, `field`, `asdict`
8. Testing — pytest asserts, raises, parametrize, fixtures
