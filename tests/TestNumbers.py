__author__ = 'edwardvella'
import unittest


class TestNumbers(unittest.TestCase):

    def test_find_pi_to_the_nth_digit(self):
        from Numbers import find_pi_to_the_nth_digit
        self.assertEqual(float(3.1415926535897913), float(find_pi_to_the_nth_digit(10)))

    def test_find_mortgage_cost_after(self):
        from Numbers import calculate_mortgage
        self.assertEqual(float(1360435.51336), calculate_mortgage(6.5, 30 * 12, 200000, 30))

if __name__ == '__main__':
    unittest.main()