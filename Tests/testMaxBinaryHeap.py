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


# Simple unittests for the ADT MaxBinaryHeap
import unittest
import random

from ADTs.AbstractDataStructures import MaxBinaryHeap


class MaxBinaryHeapTests(unittest.TestCase):

    def test_size(self):
        heap = MaxBinaryHeap()
        self.assertEqual(heap.size(), 0, "Size method is not correct")
        self.assertTrue(heap.size() == len(heap), "len(heap) method not implemented correctly")
        self.assertTrue(heap.is_empty(), "is_empty method not implemented correctly")

        heap = MaxBinaryHeap(str)
        self.assertEqual(heap.size(), 0, "Size method is not correct")
        self.assertTrue(heap.size() == len(heap), "len(heap) method not implemented correctly")
        self.assertTrue(heap.is_empty(), "is_empty method not implemented correctly")

        size = 0
        for i in ["word", "sentence", "text"]:
            heap.add(i)
            size += 1
            self.assertEqual(heap.size(), size, "Size method is not correct")
        self.assertFalse(heap.is_empty(), "is_empty method not implemented correctly")

        heap = MaxBinaryHeap()
        for i in range(10):
            heap.add(i)
            heap.peek_max()
        self.assertEqual(heap.size(), 10, "Size method is not correct")

        for i in range(5):
            heap.remove_max()
            heap.replace_root(i**2)

        self.assertEqual(heap.size(), 5, "Size method is not correct")
        heap.replace_root(33)
        self.assertFalse(heap.is_empty(), "is_empty method not implemented correctly")
        self.assertEqual(heap.size(), 5, "Size method is not correct")

    def test_type(self):
        with self.assertRaises(TypeError):
            MaxBinaryHeap(elements_type=5.4)

        with self.assertRaises(TypeError):
            MaxBinaryHeap(elements_type=None)

        heap = MaxBinaryHeap()
        self.assertEqual(heap.type(), int, "type method is not correct")

        with self.assertRaises(TypeError):
            heap.add("string")

        heap.add(23)
        with self.assertRaises(TypeError):
            heap.replace_root("word")

        for i in range(5):
            heap.add(i**2)
        heap.remove_max()
        heap.peek_max()
        self.assertEqual(heap.type(), int, "type method is not correct")

        heap = MaxBinaryHeap(str)
        self.assertEqual(heap.type(), str, "type method is not correct")

        with self.assertRaises(TypeError):
            heap.add(1.23123)

        heap.add("string")

        with self.assertRaises(TypeError):
            heap.replace_root(12)

    def test_remove_max(self):
        heap = MaxBinaryHeap()
        with self.assertRaises(ValueError):
            heap.remove_max()
        self.assertEqual(heap.peek_max(), None, "peek_max not working")

        heap.add(32)
        self.assertEqual(heap.peek_max(), 32, "peek_max not working")
        self.assertEqual(heap.remove_max(), 32, "remove_max method not working")
        self.assertEqual(heap.size(), 0, "remove_max doesn't adjust size properly")

        for num in [2, 43, 12, 234, 101, 59, 67]:
            heap.add(num)
        self.assertEqual(heap.remove_max(), 234, "remove_max method not working")
        self.assertEqual(heap.size(), 6, "remove_max doesn't adjust size properly")
        self.assertEqual(heap.peek_max(), 101, "remove_max doesn't adjust heap properly after the removal")

        heap.replace_root(0)
        self.assertEqual(67, heap.peek_max(), "peek_max is not working")
        size = heap.size()
        self.assertEqual(heap.remove_max(), 67, "remove_max doesnt work when replacing root")
        self.assertEqual(heap.size(), size - 1, "remove_max doesn't adjust size of heap properly")

    def test_add(self):
        heap = MaxBinaryHeap(str)

        with self.assertRaises(TypeError):
            heap.add(1.2)

        letters = ["g", "b", "f"]
        for string in letters:
            heap.add(string)
        self.assertEqual(heap.size(), 3, "add method doesn't adjust size")
        self.assertEqual(heap.peek_max(), "g", "add method doesn't adjust the heap properly")

        sorted_letters = heap.get_sorted_elements()
        letters.sort(reverse=True)
        for i in range(len(sorted_letters)):
            self.assertEqual(sorted_letters[i], letters[i])

        heap.add("z")
        self.assertEqual(heap.remove_max(), "z", "add method doesn't adjust the heap properly")

    def test_replace_root(self):
        heap = MaxBinaryHeap(float)

        with self.assertRaises(ValueError):
            heap.replace_root(5.4)

        for float_num in [6.343, 1.231, 2.342, 3.75, 5.6]:
            heap.add(float_num)

        with self.assertRaises(TypeError):
            heap.replace_root(5)

        self.assertEqual(heap.peek_max(), 6.343)
        heap.replace_root(2.454)
        self.assertEqual(heap.peek_max(), 5.6, "replace_root doesn't adjust heap properly")
        self.assertTrue(2.454 in heap.get_sorted_elements(), "replace_root doesn't add the element to the heap")

        heap.replace_root(7.01)
        self.assertEqual(heap.peek_max(), 7.01, "replace_root doesn't adjust heap properly")
        self.assertEqual(heap.remove_max(), 7.01, "replace_root doesn't adjust heap properly")

    def test_sorted_elements(self):
        heap = MaxBinaryHeap()
        self.assertTrue(len(heap.get_sorted_elements()) == 0)

        random_nums = [random.randint(1, 100)*x for x in range(100)]
        for num in random_nums:
            heap.add(num)

        random_nums.sort(reverse=True)
        self.assertEqual(heap.get_sorted_elements(), random_nums, "get_sorted_elements not working properly")

        random_nums.remove(max(random_nums))
        heap.remove_max()
        self.assertEqual(heap.get_sorted_elements(), random_nums, "get_sorted_elements not working properly when "
                                                                  "removing max element")
        self.assertEqual(heap.size(), len(random_nums))

    def test_iterator(self):
        heap = MaxBinaryHeap(float)

        floats = [2.5, 3.5, 4.0, 10.11, 2.79, 0.55554]
        for f in floats:
            heap.add(f)
        floats.sort(reverse=True)

        index = 0
        for f in heap:
            self.assertEqual(f, floats[index], "iterator not implemented correctly")
            index += 1

        heap = MaxBinaryHeap(str)

        strings = ["c", "db", "python", "java", "javascrpit", "ruby", "django"]
        for s in strings:
            heap.add(s)
        strings.sort(reverse=True)

        heap_iter = iter(heap)
        list_iter = iter(strings)

        while True:
            try:
                self.assertEqual(heap_iter.__next__(), list_iter.__next__(), "iterator not implemented correctly")
            except StopIteration:
                break

    def test_str(self):
        heap = MaxBinaryHeap()
        self.assertEqual(str(heap), "[]", "Wrong str implementation")

        heap.add(20)
        heap.add(100)
        heap.add(40)
        heap.add(50)
        self.assertEqual(str(heap), "[100, 50, 40, 20]", "Wrong str implementation")

    def test_replace(self):
        heap = MaxBinaryHeap()
        with self.assertRaises(KeyError):
            heap.replace(2, 10)

        heap.add(2)
        self.assertEqual(heap.peek_max(), 2)
        heap.replace(2, 100)
        self.assertEqual(heap.peek_max(), 100, "Wrong replace implementation")

        with self.assertRaises(TypeError):
            heap.replace("string", 10)

        heap.add(34)
        heap.add(60)
        heap.add(48)
        heap.add(59)
        heap.add(51)
        heap.add(48)
        self.assertEqual(str(heap), "[100, 59, 60, 34, 48, 51, 48]", "Wrong replace implementation")

        heap.replace(34, 3)
        self.assertTrue(heap.contains(3), "Wrong replace implementation")
        self.assertFalse(34 in heap, "Wrong replace implementation")
        self.assertEqual(str(heap), "[100, 59, 60, 3, 48, 51, 48]", "Wrong replace implementation")

        heap.replace(3, 101)
        self.assertTrue(heap.contains(101), "Wrong replace implementation")
        self.assertEqual(heap.peek_max(), 101, "Wrong replace implementation")
        self.assertFalse(3 in heap, "Wrong replace implementation")
        self.assertEqual(str(heap), "[101, 100, 60, 59, 48, 51, 48]")

        heap.replace(101, 1)
        self.assertTrue(heap.contains(1), "Wrong replace implementation")
        self.assertEqual(heap.peek_max(), 100, "Wrong replace implementation")
        self.assertFalse(101 in heap, "Wrong replace implementation")
        self.assertEqual(str(heap), "[100, 59, 60, 1, 48, 51, 48]")

        heap.add(51)
        heap.add(4)
        heap.replace(59, 4)
        self.assertEqual(str(heap), "[100, 51, 60, 4, 48, 51, 48, 1, 4]", "Wrong replace implementation")
        heap.replace(60, 51)
        self.assertEqual(str(heap), "[100, 51, 51, 4, 48, 51, 48, 1, 4]", "Wrong replace implementation")
        heap.replace(51, 510)
        heap.replace(4, 6)
        heap.replace(4, 5)
        self.assertEqual(str(heap), "[510, 100, 51, 6, 48, 51, 48, 1, 5]", "Wrong replace implementation")

    def test_remove(self):
        heap = MaxBinaryHeap(float)
        with self.assertRaises(KeyError):
            heap.remove(5.5)

        heap.add(5.5)
        self.assertFalse(heap.is_empty())
        with self.assertRaises(TypeError):
            heap.remove(15)
        heap.remove(5.5)
        self.assertTrue(heap.is_empty())

        heap.add(10.0)
        heap.add(11.5)
        heap.add(15.0)
        heap.add(2.3)
        heap.add(3.9)
        heap.remove(15.0)
        self.assertEqual(heap.peek_max(), 11.5, "Wrong remove implementation")
        self.assertFalse(heap.contains(15.0), "Wrong remove implementation")
        self.assertEqual(str(heap), "[11.5, 10.0, 3.9, 2.3]", "Wrong remove implementation")

        heap.add(10.9)
        heap.add(10.5)
        heap.remove(2.3)
        self.assertFalse(heap.contains(2.3), "Wrong remove implementation")
        self.assertEqual(str(heap), "[11.5, 10.9, 10.5, 3.9, 10.0]", "Wrong remove implementation")

        heap.add(2.1)
        heap.add(2.2)
        heap.add(1.1)
        heap.add(1.5)
        heap.replace(10.0, 10.7)
        heap.add(10.6)
        heap.remove(2.1)
        self.assertEqual(str(heap), "[11.5, 10.9, 10.6, 3.9, 10.7, 10.5, 2.2, 1.1, 1.5]", "Wrong remove implementation")

        heap.remove(1.5)
        self.assertEqual(str(heap), "[11.5, 10.9, 10.6, 3.9, 10.7, 10.5, 2.2, 1.1]", "Wrong remove implementation")

if __name__ == '__main__':
    unittest.main()
