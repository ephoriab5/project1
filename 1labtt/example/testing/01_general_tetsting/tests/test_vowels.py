import unittest
from vowels import count_vowels, count_symbols  # Додали імпорт count_symbols

class TestCountVowels(unittest.TestCase):

    def test_standard_string(self):
        """Звичайний рядок з голосними"""
        self.assertEqual(count_vowels("hello"), 2) # e, o

    def test_empty_string(self):
        """🔥 Тест для порожнього рядка"""
        self.assertEqual(count_vowels(""), 0)

    def test_string_with_numbers(self):
        """🔥 Тест для рядка з цифрами та приголосними"""
        self.assertEqual(count_vowels("12345! bcdf"), 0)

    def test_ukrainian_string(self):
        """🔥 Тест для рядка з українськими літерами"""
        self.assertEqual(count_vowels("Привіт світ"), 3) # И, і, і

    def test_invalid_type(self):
        """Перевірка помилки, якщо передати не рядок"""
        with self.assertRaises(TypeError):
            count_vowels(12345)

    def test_count_symbols(self):
        """Тест для підрахунку символів у рядку з методички"""
        self.assertEqual(3, count_symbols("abc"))
        self.assertEqual(0, count_symbols(""))


if __name__ == "__main__":
    unittest.main()