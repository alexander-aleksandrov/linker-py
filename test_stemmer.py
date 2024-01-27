from stemmer import stemm, is_valid
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("test", False),  
    ("кошкf", False),  
    ("кошк1", False),  
    ("к", False), 
    ("k", False),
    ("ЗеМлЯ", True),
    ("1", False)
])
def test_normalize_validates_for_cirillic(test_input, expected):
    assert is_valid(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("по", "по"),  
    ("сто", "сто"),  
    ("просто", "прост"),
])
def test_stemm_small_words(test_input, expected):
    assert stemm(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("напоминавшая", "напомина"),
    ("чакральный", "чакр"),
    ("чакра", "чакр"),
    ("прочитавший","прочит")


])
def test_stemm_long_words(test_input, expected):
    assert stemm(test_input) == expected