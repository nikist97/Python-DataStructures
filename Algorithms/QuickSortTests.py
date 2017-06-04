# Simple unittests for the quick_sort method
import unittest

from Algorithms.SortingAlgorithms import quick_sort


class QuickSortTest(unittest.TestCase):

    def test_empty(self):
        empty_list = []
        quick_sort(empty_list)
        self.assertEqual(empty_list, [], "Quick sort gives wrong results with empty lists")
        new_list = quick_sort(empty_list)
        self.assertEqual(new_list, empty_list, "Quick sort gives wrong results with empty lists")

    def test_singleton(self):
        singleton = [5]
        quick_sort(singleton)
        self.assertEqual(singleton, [5], "Quick sort gives wrong results with singletons")

        singleton = ["string"]
        sorted_singleton = quick_sort(singleton)
        self.assertEqual(sorted_singleton, singleton, "Quick sort gives wrong results with singletons")

    def test_normal_list(self):
        # no repetitions in the list
        list_of_numbers = [5, 19, 2, -122, 120, 11, 356, -47, 81, 90, 122, 47, -122]
        quick_sort(list_of_numbers)
        self.assertEqual(list_of_numbers, [-122, -122, -47, 2, 5, 11, 19, 47, 81, 90, 120, 122, 356],
                         "Quick sort gives wrong results with a list with no repetitions")

        # repetitions in the list
        list_of_numbers = [5, 19, 2, 122, 120, 11, 356, 47, 81, 90, 2, 2, 5, 122, 123]
        new_list_of_numbers = quick_sort(list_of_numbers)
        self.assertEqual(new_list_of_numbers, [2, 2, 2, 5, 5, 11, 19, 47, 81, 90, 120, 122, 122, 123, 356],
                         "Quick sort gives wrong results with a list with no repetitions")

        # random list
        import random
        quick_sorted_list = []
        python_sorted_list = []
        for i in range(50):
            num = random.randint(1, 100)
            quick_sorted_list.append(num)
            python_sorted_list.append(num)
        python_sorted_list.sort()

        self.assertEqual(quick_sort(quick_sorted_list), python_sorted_list,
                         "Quick sort produces wrong results with random list")

        # testing strings with no repetitions
        strings_list = ["world", "hello", "python", "programming", "coding", "test"]
        quick_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "coding", "test"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Quick sort produces wrong results with strings with no repetitions")

        # testing strings with repetitions
        strings_list = ["world", "hello", "python", "programming", "code", "test", "world", "hello", "python", "hello"]
        quick_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "code", "test", "world", "hello", "python",
                                 "hello"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Quick sort produces wrong results with strings with repetitions")

if __name__ == '__main__':
    unittest.main()
