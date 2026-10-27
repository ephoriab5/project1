import unittest
from app import Figure

class TestFigure(unittest.TestCase):

    def test_figure_properties(self):
        """Перевірка звичайних властивостей фігури"""
        fig = Figure("квадрат", 5.0)
        self.assertEqual(fig.get_figure_type, "квадрат")
        self.assertEqual(fig.get_figure_length, 5.0)

    def test_get_angles(self):
        """Перевірка кількості кутів для різних фігур"""
        square = Figure("квадрат", 4)
        rectangle = Figure("прямокутник", 6)
        triangle = Figure("трикутник", 3)

        self.assertEqual(square.get_angles, 4)
        self.assertEqual(rectangle.get_angles, 4)
        self.assertEqual(triangle.get_angles, 3)

    def test_invalid_length(self):
        """Перевірка виникнення помилки для нульової та від'ємної довжини"""
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)
        with self.assertRaises(ValueError):
            Figure("трикутник", -2.5)

    def test_unknown_figure_type(self):
        """Перевірка помилки для невідомого типу фігури"""
        fig = Figure("коло", 5)
        with self.assertRaises(ValueError):
            _ = fig.get_angles

    def test_figure_lengths_subtest(self):
        """Приклад використання subTest для перевірки кількох значень"""
        for length in [1, 5, 10]:
            with self.subTest(length=length):
                fig = Figure("квадрат", length)
                self.assertEqual(fig.get_figure_length, length)


if __name__ == "__main__":
    unittest.main()