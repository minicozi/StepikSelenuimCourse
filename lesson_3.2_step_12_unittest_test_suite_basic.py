import unittest


class TestAbs(unittest.TestCase):  # Имя класса должно быть Test*

    def test_abs1(self):  # Имя теста должно быть test_*
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()