# ------------------------------------------- 4 -----------------------------
"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from string import ascii_letters

import pytest


def filter_lower(s: str) -> str:
    result = ''.join(char for char in s if char in set(ascii_letters + ' '))
    return result.lower()


def test_no_change():
    input_text = "This is a sample text with 123 numbers and punctuation!"
    result = filter_lower(input_text)
    assert result == "this is a sample text with 123 numbers and punctuation!"


def test_change_case():
    input_text = "UpperCase And LOWERCASE"
    result = filter_lower(input_text)
    assert result == "uppercase and lowercase"


def test_remove_punctuation():
    input_text = "Text with, some. punctuation!"
    result = filter_lower(input_text)
    assert result == "text with some punctuation"


def test_remove_non_latin_chars():
    input_text = "Пример текста на русском языке"
    result = filter_lower(input_text)
    assert result == "    "


def test_combined_changes():
    input_text = "Th!s Is a TeXt w1th Üñicödè"
    result = filter_lower(input_text)
    assert result == "ths is a text w1th cd"


if __name__ == '__main__':
    pytest.main(['-v'])
