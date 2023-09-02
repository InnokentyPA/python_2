# ------------------------------------------- 3 -----------------------------
"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

import unittest
from string import ascii_letters


def filter_lower(s: str) -> str:
    result = ''.join(char for char in s if char in set(ascii_letters + ' '))
    return result.lower()


class TestFilterLower(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('hi bro', filter_lower('hi bro'))

    def test_lower(self):
        self.assertEqual('hello world', filter_lower('Hello world'))

    def test_punctuation(self):
        self.assertEqual('hello my friend', filter_lower('hello, my friend!'))

    def test_languages(self):
        self.assertEqual('   hello', filter_lower('привет переводится как hello'))

    def test_all(self):
        self.assertEqual('hello    jony', filter_lower('Hello, мой дорогой друг Jony!'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
