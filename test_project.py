from stemmer import stemm, is_valid
from project import normalize_file_names, replace_outside_brackets
import pytest

@pytest.mark.parametrize("test_input,expected", [
        # one word file name
       (["Ключики.md"], {"Ключики.md": ["ключики"]}),
        # two and more words file name
       (["Понимание работы.md", "Ключики моменты работы.md"], {"Понимание работы.md": ["пониман", "раб"], "Ключики моменты работы.md": ["ключ", "момент", "раб"]}),
])
def test_normalize_file_names(test_input, expected):
    assert normalize_file_names(test_input) == expected

@pytest.mark.parametrize("text, word_to_replace, replacement, expected", [
    ("[[Ключики|ключики]] ключами нам ", "ключами", "[[Ключики|ключами]]", "[[Ключики|ключики]] [[Ключики|ключами]] нам "),
])
def test_replace_outside_brackets(text, word_to_replace, replacement, expected):
    assert replace_outside_brackets(text, word_to_replace, replacement) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("test", False),  
    ("кошкf", False),  
    ("кошк1", False),  
    ("к", False), 
    ("k", False),
    ("ЗеМлЯ", True),
    ("1", False)
])
def test_is_valid_for_cirillic(test_input, expected):
    assert is_valid(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("по", "по"),  
    ("сто", "сто"),  
    ("просто", "прост"),
])
def test_stemm_small_words(test_input, expected):
    assert stemm(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("носорог", "носорог"),
    ("рыбам", "рыб"),
    ("котики", "кот"),
    ("солнце","солнц"),
    ("пропажа", "пропаж"),
])
def test_stemm_noun(test_input, expected):
    assert stemm(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("учитель", "уч"),
    ("речка", "реч"),
    ("ключик", "ключ"),
    ("цветник","цвет"),
    ("домище", "дом"),
    ("каменщик", "камен"),
    ("газетчик", "газетч"),
])
def test_stemm_noun_with_suffix(test_input, expected):
    assert stemm(test_input) == expected
