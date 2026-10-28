import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "34_check_sorted.py"
spec = importlib.util.spec_from_file_location("program34", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_empty_list():
    assert module.is_sorted([]) is True