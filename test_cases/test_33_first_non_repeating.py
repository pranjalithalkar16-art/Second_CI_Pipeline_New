import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "33_first_non_repeating.py"
spec = importlib.util.spec_from_file_location("program33", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_normal_string():
    assert module.first_non_repeating("aabbcdd") == "c"


def test_first_character():
    assert module.first_non_repeating("abcabcde") == "d"


def test_no_unique_character():
    assert module.first_non_repeating("aabb") == ""