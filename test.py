import unittest
from main import count_letters
from main import count_unique
from main import sum_consecutives
from main import increment_string

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

class Test_count_unique(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(count_unique("hi hey hi"), 2)

    def test_empty_string(self):
        self.assertEqual(count_unique(" "), 0)

    def test_one_word(self):
        self.assertEqual(count_unique("hello"), 1)

    def test_case_insesnitivity(self):
        self.assertEqual(count_unique("Hi hey hi"), 3)

    def test_number_string(self):
        self.assertEqual(count_unique("345 hey 345"), 2)
    
    def test_not_a_string(self):
        with self.assertRaises(TypeError):
            count_unique(345)
    
class Test_sum_consecutives(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sum_consecutives([1, 2, 3]), [3, 5])
    
    def test_one_number(self):
        self.assertEqual(sum_consecutives([1]), [])

    def test_empty_list(self):
        self.assertEqual(sum_consecutives([]), [])

    def test_negatives(self):
        self.assertEqual(sum_consecutives([-1, -2, -3]), [-3, -5])


class TestIncrementString(unittest.TestCase):
    def test_no_number(self):
        self.assertEqual(increment_string("foo"), "foo1")

    def test_with_number(self):
        self.assertEqual(increment_string("foo42"), "foo43")

    def test_with_zeroes(self):
        self.assertEqual(increment_string("foo0042"), "foo0043")
    
    def test_with_9(self): 
        self.assertEqual(increment_string("foo099"), "foo100")



if __name__ == "__main__":
    unittest.main()