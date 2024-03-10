import unittest
from app_file import mult

class TestMultiplication(unittest.TestCase):
    def test_mult_0(self):
        self.assertEqual(mult(5, 8), 40) # Corrected the expected result to 40

    def test_mult_1(self):
        self.assertEqual(mult(2, 4), 8) # Corrected the expected result to 8

    def test_mult_2(self):
        self.assertEqual(mult(5, 5), 25)

if __name__ == '__main__':
    unittest.main()
