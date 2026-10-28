from pathlib import Path
import importlib.util

file_path = Path(__file__).parent.parent / "codes" / "32_count_words.py"
spec = importlib.util.spec_from_file_location("count_words", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_count_words():
    assert module.count_words("I love Python") == 3


def test_empty_sentence():
    assert module.count_words("") == 0


def test_extra_spaces():
    assert module.count_words("Hello   world") == 2