import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "31_pangram.py"
spec = importlib.util.spec_from_file_location("pangram", file_path)
pangram = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pangram)


def test_pangram():
    assert pangram.is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_not_pangram():
    assert pangram.is_pangram("Hello world") is False