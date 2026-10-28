import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "37_rotate_string.py"
spec = importlib.util.spec_from_file_location("program37", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_rotate_two_positions():
    assert module.rotate_string("hello", 2) == "lohel"


def test_rotate_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"


def test_empty_string():
    assert module.rotate_string("", 3) == ""


def test_large_rotation():
    assert module.rotate_string("abc", 4) == "cab"