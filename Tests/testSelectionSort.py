"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# Simple unittests for the selection_sort method
import unittest

from Algorithms.SortingAlgorithms import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_empty(self):
        empty_list = []
        selection_sort(empty_list)
        self.assertEqual(empty_list, [], "Selection sort gives wrong results with empty lists")
        new_list = selection_sort(empty_list)
        self.assertEqual(new_list, empty_list, "Selection sort gives wrong results with empty lists")

    def test_singleton(self):
        singleton = [5]
        selection_sort(singleton)
        self.assertEqual(singleton, [5], "Selection sort gives wrong results with singletons")

        singleton = ["string"]
        sorted_singleton = selection_sort(singleton)
        self.assertEqual(sorted_singleton, singleton, "Selection sort gives wrong results with singletons")

    def test_normal_list(self):
        # no repetitions in the list
        list_of_numbers = [5, 19, 2, -122, 120, 11, 356, -47, 81, 90, 122, 47, -122]
        selection_sort(list_of_numbers)
        self.assertEqual(list_of_numbers, [-122, -122, -47, 2, 5, 11, 19, 47, 81, 90, 120, 122, 356],
                         "Selection sort gives wrong results with a list with no repetitions")

        # repetitions in the list
        list_of_numbers = [5, 19, 2, 122, 120, 11, 356, 47, 81, 90, 2, 2, 5, 122, 123]
        new_list_of_numbers = selection_sort(list_of_numbers)
        self.assertEqual(new_list_of_numbers, [2, 2, 2, 5, 5, 11, 19, 47, 81, 90, 120, 122, 122, 123, 356],
                         "Selection sort gives wrong results with a list with no repetitions")

        # random list
        import random
        selection_sorted_list = []
        python_sorted_list = []
        for i in range(50):
            num = random.randint(1, 100)
            selection_sorted_list.append(num)
            python_sorted_list.append(num)
        python_sorted_list.sort()

        self.assertEqual(selection_sort(selection_sorted_list), python_sorted_list,
                         "Selection sort produces wrong results with random list")

        # testing strings with no repetitions
        strings_list = ["world", "hello", "python", "programming", "coding", "Tests"]
        selection_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "coding", "Tests"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Selection sort produces wrong results with strings with no repetitions")

        # testing strings with repetitions
        strings_list = ["world", "hello", "python", "programming", "code", "Tests", "world", "hello", "python", "hello"]
        selection_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "code", "Tests", "world", "hello", "python",
                                 "hello"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Selection sort produces wrong results with strings with repetitions")

if __name__ == '__main__':
    unittest.main()
