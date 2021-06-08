import reverse
import unittest

class TestCase(unittest.TestCase):
    def test_reverse_1(self):
        self.assertEqual(reverse.reverse("My name is V Tadimeti"), "Tadimeti V is name My")

    def test_reverse_2(self):
        self.assertEqual(reverse.reverse("Some String"), "String Some")

if __name__ == "__main__":
    unittest.main()