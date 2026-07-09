# =============================================================
# ADVANCED 8: TESTING WITH PYTEST
# =============================================================
#
# BIG IDEA:
#   Tests are executable specs. pytest finds functions named
#   test_* and reports failures clearly.
#
#   This file is BOTH a lesson and a tiny test suite.
#   Run with:
#       pip install pytest          # once, in a venv
#       pytest advanced/08_testing_pytest.py -v
#
#   Or run as a script — it falls back to a mini runner if
#   pytest isn't installed.
# =============================================================


# --- Step 1: Code under test ---------------------------------
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def average(nums):
    if not nums:
        raise ValueError("empty list")
    return sum(nums) / len(nums)


# --- Step 2: Basic assertions --------------------------------
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_average():
    assert average([1, 2, 3]) == 2.0


# --- Step 3–5: pytest-only features (skipped if not installed) ---
# assert expression            # fail if False
# pytest.raises(Exc)           # expect an error
# @pytest.mark.parametrize     # table-driven tests
# @pytest.fixture              # shared setup injected into tests
#
# Layout tip (real projects):
#   src/myapp/...
#   tests/test_....py

try:
    import pytest
except ImportError:  # pragma: no cover
    pytest = None


if pytest is not None:

    def test_divide_by_zero():
        with pytest.raises(ValueError, match="cannot divide"):
            divide(10, 0)

    def test_average_empty():
        with pytest.raises(ValueError):
            average([])

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 1, 2),
            (0, 5, 5),
            (-2, -3, -5),
            (100, 0, 100),
        ],
    )
    def test_add_many(a, b, expected):
        assert add(a, b) == expected

    @pytest.fixture
    def sample_nums():
        return [10, 20, 30]

    def test_average_with_fixture(sample_nums):
        assert average(sample_nums) == 20.0


# =============================================================
# TRY IT YOURSELF:
#   1. Add `test_divide_ok` asserting divide(9, 3) == 3.
#   2. Run: pytest advanced/08_testing_pytest.py -v
# =============================================================


def test_divide_ok():
    assert divide(9, 3) == 3


# =============================================================
# Script fallback — run without pytest installed
# =============================================================
if __name__ == "__main__":
    print("===== Advanced 8: pytest lesson =====")
    print("""
Run the real suite with:
  python3 -m venv .venv && source .venv/bin/activate
  pip install pytest
  pytest advanced/08_testing_pytest.py -v
""")
    # Manual stand-ins for raises / parametrize / fixture ideas:
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"  PASS raises check: {e}")

    for a, b, expected in [(1, 1, 2), (0, 5, 5), (-2, -3, -5)]:
        assert add(a, b) == expected
    print("  PASS parametrize stand-in")

    sample_nums = [10, 20, 30]
    assert average(sample_nums) == 20.0
    print("  PASS fixture stand-in")

    simple_tests = [test_add, test_average, test_divide_ok]
    for fn in simple_tests:
        fn()
        print(f"  PASS {fn.__name__}")
    print("\nSimple demos passed (install pytest for the full suite).")