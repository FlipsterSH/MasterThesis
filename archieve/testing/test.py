import unittest
from supporting_functions import percent_difference, calculate_percent_differences, trim_lists_to_same_length, round_to_nearest_half



# Unit test class for percent_difference function
class TestPercentDifference(unittest.TestCase):

    def test_positive_difference(self):
        # Test case where the after value is greater than the before value
        self.assertAlmostEqual(percent_difference(50, 75), 50.0)

    def test_negative_difference(self):
        # Test case where the after value is less than the before value
        self.assertAlmostEqual(percent_difference(100, 50), -50.0)

    def test_zero_before(self):
        # Test case where the before value is 0
        self.assertEqual(percent_difference(0, 100), "Zerodivision attempted in percent_difference()")

    def test_no_difference(self):
        # Test case where the before and after values are the same
        self.assertAlmostEqual(percent_difference(50, 50), 0.0)

    def test_after_zero(self):
        # Test case where the after value is 0 and before is positive
        self.assertAlmostEqual(percent_difference(50, 0), -100.0)



# class TestCalculatePercentDifferences(unittest.TestCase):

#     def test_increasing_prices(self):
#         # Test with increasing stock prices
#         prices = [100, 105, 110, 115]
#         expected = [5.0, 4.76, 4.55]
#         result = calculate_percent_differences(prices)
#         self.assertEqual([round(val, 2) for val in result], expected)

#     def test_decreasing_prices(self):
#         # Test with decreasing stock prices
#         prices = [115, 110, 105, 100]
#         expected = [-4.35, -4.55, -4.76]
#         result = calculate_percent_differences(prices)
#         self.assertEqual([round(val, 2) for val in result], expected)

#     def test_mixed_prices(self):
#         # Test with mixed stock prices (both increases and decreases)
#         prices = [100, 200, 400, 800]
#         expected = [100, 100, 100]
#         result = calculate_percent_differences(prices)
#         self.assertEqual(result, expected)

#     def test_single_price(self):
#         # Test with a single price (should return an empty list)
#         prices = [100]
#         expected = []
#         result = calculate_percent_differences(prices)
#         self.assertEqual(result, expected)

#     def test_empty_list(self):
#         # Test with an empty list (should return an empty list)
#         prices = []
#         expected = "error with input into calculate_percent_difference()"
#         result = calculate_percent_differences(prices)
#         self.assertEqual(result, expected)



class TestTrimListsToSameLength(unittest.TestCase):

    def test_equal_length_lists(self):
        list1 = [10, 20, 30, 40, 50]
        list2 = [15, 25, 35, 45, 55]
        expected_list1 = [10, 20, 30, 40, 50]
        expected_list2 = [15, 25, 35, 45, 55]
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertEqual(trimmed_list1, expected_list1)
        self.assertEqual(trimmed_list2, expected_list2)

    def test_list1_longer_than_list2(self):
        list1 = [10, 20, 30, 40, 50]
        list2 = [15, 25, 35]
        expected_list1 = [30, 40, 50]
        expected_list2 = [15, 25, 35]
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertEqual(trimmed_list1, expected_list1)
        self.assertEqual(trimmed_list2, expected_list2)

    def test_list2_longer_than_list1(self):
        list1 = [10, 20, 30]
        list2 = [15, 25, 35, 45, 55]
        expected_list1 = [10, 20, 30]
        expected_list2 = [35, 45, 55]
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertEqual(trimmed_list1, expected_list1)
        self.assertEqual(trimmed_list2, expected_list2)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        expected = "List has no length error in trim_lists_to_same_length()"
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertEqual(trimmed_list1, "List has no length error in trim_lists_to_same_length()")

    def test_one_empty_list(self):
        list1 = [10, 20, 30, 40, 50]
        list2 = []
        expected = "List has no length error in trim_lists_to_same_length()"
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertEqual(trimmed_list1, "List has no length error in trim_lists_to_same_length()")

    def fail_test(self):
        list1 = [10, 20, 30, 40, 50]
        list2 = [20, 30, 40]
        expected_list1 = [10, 20, 30]
        expected_list2 = [20, 30, 40]
        trimmed_list1, trimmed_list2 = trim_lists_to_same_length(list1, list2)
        self.assertNotEqual(trimmed_list1, expected_list1)




class TestRoundToNearestHalf(unittest.TestCase):

    def test_rounding(self):
        # Test cases with expected outputs
        test_cases = [
            ([1.3, 2.7, 3.8, 4.1, 5.5, 6.2], [1.5, 2.5, 4.0, 4.0, 5.5, 6.0]),
            ([0.1, 0.4, 0.6, 0.9], [0.0, 0.5, 0.5, 1.0]),
            ([2.25, 2.75, 3.125], [2.0, 3.0, 3.0]),
            ([-1.3, -2.7, -3.8], [-1.5, -2.5, -4.0]),
            ([0, 2.5, 5.5], [0.0, 2.5, 5.5])
        ]
        
        for data, expected in test_cases:
            result = round_to_nearest_half(data)
            self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()