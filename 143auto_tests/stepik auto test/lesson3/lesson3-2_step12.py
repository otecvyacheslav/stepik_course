import unittest  # импорт юнитеста


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "should be absolute value of a number")
if __name__ == "__main__":
    unittest.main()