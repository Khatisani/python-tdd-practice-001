import unittest
from main import count_letters

class Test_count_letters(unittest.TestCase):
    def test_normal_word(self):
        self.assertEqual(count_letters("car"), {'c':1, 'a':1, 'r':1})

    def test_empty_string(self):
        self.assertEqual(count_letters(""), {})

    def test_one_letter(self):
        self.assertEqual(count_letters("c"), {'c':1})

    def test_duplicates(self):
        self.assertEqual(count_letters("apple"), {"a":1,"p":2,"l":1,"e":1})

    def test_upper_lower(self):
        self.assertEqual(count_letters("Aa"), {"A":1,"a":1})

    def test_with_special_char(self):
        self.assertEqual(count_letters("a)b"), {"a":1,"b":1})

    def test_with_numbers(self):
        self.assertEqual(count_letters("A2B6"), {"A":1,"B":1})
    
    def test_not_a_string(self):
        with self.assertRaises(TypeError):
            count_letters(345)

    

if __name__ == "__main__":
    unittest.main()