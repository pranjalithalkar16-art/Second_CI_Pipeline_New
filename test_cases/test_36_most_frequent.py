import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "36_most_frequent.py"
spec = importlib.util.spec_from_file_location("program36", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_most_frequent():
    assert module.most_frequent([1, 2, 2, 3, 2]) == 2


def test_tie():
    assert module.most_frequent([1, 1, 2, 2]) == 1


def test_empty_list():
    assert module.most_frequent([]) is None