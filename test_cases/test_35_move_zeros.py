import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "35_move_zeros.py"
spec = importlib.util.spec_from_file_location("program35", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_move_zeros():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert module.move_zeros([0, 0]) == [0, 0]