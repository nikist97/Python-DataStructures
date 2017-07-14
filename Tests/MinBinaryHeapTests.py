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


# Simple unittests for the ADT MinBinaryHeap
import unittest
import random

from ADTs.AbstractDataStructures import MinBinaryHeap


class MinBinaryHeapTests(unittest.TestCase):

    def test_size(self):
        heap = MinBinaryHeap()
        self.assertEqual(heap.size(), 0, "Size method is not correct")
        self.assertTrue(heap.size() == len(heap), "len(heap) method not implemented correctly")
        self.assertTrue(heap.is_empty(), "is_empty method not implemented correctly")

        heap = MinBinaryHeap(str)
        self.assertEqual(heap.size(), 0, "Size method is not correct")
        self.assertTrue(heap.size() == len(heap), "len(heap) method not implemented correctly")
        self.assertTrue(heap.is_empty(), "is_empty method not implemented correctly")

        size = 0
        for i in ["word", "sentence", "text"]:
            heap.add(i)
            size += 1
            self.assertEqual(heap.size(), size, "Size method is not correct")
        self.assertFalse(heap.is_empty(), "is_empty method not implemented correctly")

        heap = MinBinaryHeap()
        for i in range(10):
            heap.add(i)
            heap.peek_min()
        self.assertEqual(heap.size(), 10, "Size method is not correct")

        for i in range(5):
            heap.remove_min()
            heap.replace_root(i**2)

        self.assertEqual(heap.size(), 5, "Size method is not correct")
        heap.replace_root(313)
        self.assertFalse(heap.is_empty(), "is_empty method not implemented correctly")
        self.assertEqual(heap.size(), 5, "Size method is not correct")

    def test_type(self):
        with self.assertRaises(TypeError):
            heap = MinBinaryHeap(elements_type=5.4)

        with self.assertRaises(TypeError):
            heap = MinBinaryHeap(elements_type=None)

        heap = MinBinaryHeap()
        self.assertEqual(heap.type(), int, "type method is not correct")

        with self.assertRaises(TypeError):
            heap.add("string")

        heap.add(23)
        with self.assertRaises(TypeError):
            heap.replace_root("word")

        for i in range(5):
            heap.add(i**2)
        heap.remove_min()
        heap.peek_min()
        self.assertEqual(heap.type(), int, "type method is not correct")

        heap = MinBinaryHeap(str)
        self.assertEqual(heap.type(), str, "type method is not correct")

        with self.assertRaises(TypeError):
            heap.add(1.23123)

        heap.add("string")

        with self.assertRaises(TypeError):
            heap.replace_root(12)

    def test_remove_min(self):
        heap = MinBinaryHeap()
        with self.assertRaises(ValueError):
            heap.remove_min()
        self.assertRaises(heap.peek_min(), None, "peek_min not working")

        heap.add(32)
        self.assertEqual(heap.peek_min(), 32, "peek_min not working")
        self.assertEqual(heap.remove_min(), 32, "remove_min method not working")
        self.assertEqual(heap.size(), 0, "remove_min doesn't adjust size properly")

        for num in [2, 43, 12, 234, 101, 59, 67]:
            heap.add(num)
        self.assertEqual(heap.remove_min(), 2, "remove_min method not working")
        self.assertEqual(heap.size(), 6, "remove_min doesn't adjust size properly")
        self.assertEqual(heap.peek_min(), 12, "remove_min doesn't adjust heap properly after the removal")

        heap.replace_root(0)
        self.assertEqual(0, heap.peek_min(), "peek_min is not working")
        size = heap.size()
        self.assertEqual(heap.remove_min(), 0, "remove_min doesnt work when replacing root")
        self.assertEqual(heap.size(), size - 1, "remove_min doesn't adjust size of heap properly")

    def test_add(self):
        heap = MinBinaryHeap(str)

        with self.assertRaises(TypeError):
            heap.add(1.2)

        letters = ["g", "b", "f"]
        for string in letters:
            heap.add(string)
        self.assertEqual(heap.size(), 3, "add method doesn't adjust size")
        self.assertEqual(heap.peek_min(), "b", "add method doesn't adjust the heap properly")

        sorted_letters = heap.get_sorted_elements()
        letters.sort()
        for i in range(len(sorted_letters)):
            self.assertEqual(sorted_letters[i], letters[i])

        heap.add("a")
        self.assertEqual(heap.remove_min(), "a", "add method doesn't adjust the heap properly")

    def test_replace_root(self):
        heap = MinBinaryHeap(float)

        with self.assertRaises(ValueError):
            heap.replace_root(5.4)

        for float_num in [6.343, 1.231, 2.342, 3.75, 5.6]:
            heap.add(float_num)

        with self.assertRaises(TypeError):
            heap.replace_root(5)

        self.assertEqual(heap.peek_min(), 1.231)
        heap.replace_root(2.454)
        self.assertEqual(heap.peek_min(), 2.342, "replace_root doesn't adjust heap properly")
        self.assertTrue(2.454 in heap.get_sorted_elements(), "replace_root doesn't add the element to the heap")

        heap.replace_root(0.01)
        self.assertEqual(heap.peek_min(), 0.01, "replace_root doesn't adjust heap properly")
        self.assertEqual(heap.remove_min(), 0.01, "replace_root doesn't adjust heap properly")

    def test_sorted_elements(self):
        heap = MinBinaryHeap()
        self.assertTrue(len(heap.get_sorted_elements()) == 0)

        random_nums = [random.randint(1, 100)*x for x in range(100)]
        for num in random_nums:
            heap.add(num)

        random_nums.sort()
        self.assertEqual(heap.get_sorted_elements(), random_nums, "get_sorted_elements not working properly")

        random_nums.remove(min(random_nums))
        heap.remove_min()
        self.assertEqual(heap.get_sorted_elements(), random_nums, "get_sorted_elements not working properly when "
                                                                  "removing min element")
        self.assertEqual(heap.size(), len(random_nums))

    def test_iterator(self):
        heap = MinBinaryHeap(float)

        floats = [2.5, 3.5, 4.0, 10.11, 2.79, 0.55554]
        for f in floats:
            heap.add(f)
        floats.sort()

        index = 0
        for f in heap:
            self.assertEqual(f, floats[index], "iterator not implemented correctly")
            index += 1

        heap = MinBinaryHeap(str)

        strings = ["c", "db", "python", "java", "javascrpit", "ruby", "django"]
        for s in strings:
            heap.add(s)
        strings.sort()

        heap_iter = iter(heap)
        list_iter = iter(strings)

        while True:
            try:
                self.assertEqual(heap_iter.__next__(), list_iter.__next__(), "iterator not implemented correctly")
            except StopIteration:
                break

    def test_str(self):
        heap = MinBinaryHeap()
        self.assertEqual(str(heap), "[]", "Wrong str implementation")

        heap.add(20)
        heap.add(100)
        heap.add(40)
        heap.add(50)
        self.assertEqual(str(heap), "[20, 50, 40, 100]", "Wrong str implementation")

if __name__ == '__main__':
    unittest.main()
