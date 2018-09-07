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


import unittest

from DataStructures.AbstractDataStructures import DuplicatePriorityQueue
from DataStructures.Errors import *


class DuplicatePriorityQueueTest(unittest.TestCase):
    def test_size(self):
        priority_queue = DuplicatePriorityQueue()
        self.assertEqual(len(priority_queue), 0, "Priority queue is not initialised as empty")
        priority_queue = DuplicatePriorityQueue(float, True)
        self.assertEqual(priority_queue.size, 0, "Priority queue is not initialised as empty")
        priority_queue = DuplicatePriorityQueue(elements_type=int, reverse=False)
        self.assertEqual(len(priority_queue), 0, "Priority queue is not initialised as empty")
        self.assertTrue(priority_queue.size == 0, "Priority queue is not initialised as empty")
        self.assertEqual(priority_queue.size, 0, "Priority queue is not initialised as empty")

        priority_queue.enqueue(5, 10)
        priority_queue.enqueue(20, 3)
        self.assertEqual(priority_queue.size, 2, "Wrong size implementation")
        self.assertEqual(len(priority_queue), 2, "Wrong len implementation")

        priority_queue = DuplicatePriorityQueue(reverse=False)
        priority_queue.enqueue(20, 3)
        priority_queue.peek()
        priority_queue.enqueue(2, 2)
        priority_queue.enqueue(10, 3)
        self.assertEqual(priority_queue.size, 3, "Wrong size implementation")

        priority_queue.dequeue()
        priority_queue.get_element(1024)
        priority_queue.enqueue(10, 2)
        priority_queue.enqueue(10, 2)
        self.assertEqual(len(priority_queue), 4, "Wrong len implementation")

    def test_type(self):
        with self.assertRaises(PriorityQueueTypeError):
            DuplicatePriorityQueue(elements_type=5.4)

        priority_queue = DuplicatePriorityQueue()
        self.assertEqual(priority_queue.type, None, "Wrong type at initialization")
        priority_queue.enqueue(5, 5)
        priority_queue.enqueue("word", 10)
        priority_queue = DuplicatePriorityQueue(str, True)
        priority_queue.enqueue("word", 5)
        priority_queue.enqueue("word", 5)
        priority_queue.enqueue("another_word", 5)
        self.assertEqual(priority_queue.type, str, "Wrong type at initialization")

        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.enqueue(2, 3)

        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.enqueue("2", "3")

        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.contains_priority(5.43)

        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.get_element("7")

    def test_reverse(self):
        priority_queue = DuplicatePriorityQueue()
        self.assertFalse(priority_queue.reversed, "Wrong reverse implementation")
        priority_queue.enqueue(1, 10)
        priority_queue.enqueue("word", 5)
        self.assertEqual(priority_queue.peek(), 1, "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), 1, "Wrong reverse implementation")

        priority_queue = DuplicatePriorityQueue(int, False)
        self.assertFalse(priority_queue.reversed, "Wrong reverse implementation")
        priority_queue.enqueue(1, 10)
        priority_queue.enqueue(5, 10)
        priority_queue.enqueue(2, 5)
        priority_queue.enqueue(2, 5)
        self.assertEqual(priority_queue.peek(), 1, "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), 1, "Wrong reverse implementation")

        priority_queue = DuplicatePriorityQueue(elements_type=str, reverse=True)
        self.assertTrue(priority_queue.reversed, "Wrong reverse implementation")
        priority_queue.enqueue("python", 1)
        priority_queue.enqueue("word", 2)
        self.assertEqual(priority_queue.peek(), "python", "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), "python", "Wrong reverse implementation")

        priority_queue = DuplicatePriorityQueue(reverse=True)
        self.assertTrue(priority_queue.reversed, "Wrong reverse implementation")

        priority_queue.enqueue(1, 10)
        priority_queue.enqueue("word", 5)
        priority_queue.enqueue("another word", 5)
        priority_queue.enqueue("word", 10)
        self.assertEqual(priority_queue.peek(), "word", "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), "word", "Wrong reverse implementation")
        self.assertEqual(priority_queue.dequeue(), "another word", "Wrong reverse implementation")

    def test_str(self):
        priority_queue = DuplicatePriorityQueue()
        self.assertEqual(str(priority_queue), "{}", "Wrong str implementation")
        priority_queue = DuplicatePriorityQueue(float, True)
        self.assertEqual(str(priority_queue), "{}", "Wrong str implementation")

        priority_queue.enqueue(1.2, 2)
        self.assertEqual(str(priority_queue), "{2: 1.2}", "Wrong str implementation")
        priority_queue.enqueue(2.5, 2)
        self.assertNotEqual(str(priority_queue), "{2: 2.5}", "Wrong str implementation")

    def test_contains(self):
        priority_queue = DuplicatePriorityQueue()
        self.assertFalse(priority_queue.contains_priority(5), "Contains fails with empty queue")
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.contains_priority("7")

        self.assertFalse(priority_queue.contains_element("7"), "Contains_element fails")

        priority_queue = DuplicatePriorityQueue(int, True)
        for i in range(10):
            priority_queue.enqueue(i**2, i)

        for j in range(10):
            self.assertTrue(priority_queue.contains_priority(j), "Wrong contains implementation")
            self.assertTrue(priority_queue.contains_element(j**2), "Contains_element fails")
            self.assertTrue(j**2 in priority_queue, "Contains_element fails")

        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.contains_element("word")

        priority_queue.enqueue(1000, 0)
        priority_queue.enqueue(25, 1)
        self.assertTrue(priority_queue.contains_priority(0), "Wrong contains implementation")
        self.assertTrue(priority_queue.contains_element(1000), "Contains_element fails")
        self.assertTrue(priority_queue.contains_element(0), "Contains_element fails")
        self.assertTrue(priority_queue.contains_element(25), "Contains_element fails")
        self.assertTrue(priority_queue.contains_element(1), "Contains_element fails")

    def test_enqueue(self):
        priority_queue = DuplicatePriorityQueue(float, False)
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.enqueue(5, 5)
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.enqueue(5.25, "5")

        d = {5: 10.5, 1: 2.7, 3: 4.90, 11: 3.14}
        for key in d:
            priority_queue.enqueue(d[key], key)

        self.assertEqual(len(priority_queue), len(d))

        for priority in d:
            self.assertFalse(priority_queue.get_element(priority) is None)
            self.assertEqual(d[priority], priority_queue.get_element(priority))

        priority_queue.enqueue(3.14, 11)
        priority_queue.enqueue(5.5, 3)
        self.assertEqual(priority_queue.dequeue(), 3.14, "Wrong enqueue implementation")
        self.assertEqual(priority_queue.dequeue(), 3.14, "Wrong enqueue implementation")
        self.assertEqual(len(priority_queue), len(d), "Wrong enqueue implementation")
        self.assertTrue(priority_queue.contains_element(5.5), "Wrong enqueue implementation")
        self.assertTrue(priority_queue.contains_element(4.90), "Wrong enqueue implementation")

    def test_dequeue(self):
        priority_queue = DuplicatePriorityQueue(str, True)
        with self.assertRaises(EmptyPriorityQueueError):
            priority_queue.dequeue()
        priority_queue.enqueue("word", 2)
        priority_queue.enqueue("python", 10)
        priority_queue.enqueue("another_word", 1)
        self.assertEqual(priority_queue.dequeue(), "another_word", "Wrong dequeue implementation")
        self.assertEqual(len(priority_queue), 2)

        priority_queue = DuplicatePriorityQueue(int, False)
        with self.assertRaises(EmptyPriorityQueueError):
            priority_queue.dequeue()
        priority_queue.enqueue(15, 2)
        priority_queue.enqueue(15, 3)
        priority_queue.enqueue(423, 10)
        priority_queue.enqueue(421, 10)
        priority_queue.enqueue(20, 1)
        priority_queue.enqueue(20, 1)
        self.assertEqual(priority_queue.dequeue(), 423, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 421, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 15, "Wrong dequeue implementation")
        self.assertEqual(len(priority_queue), 3)

    def test_iterator(self):
        priority_queue = DuplicatePriorityQueue()
        with self.assertRaises(StopIteration):
            next(iter(priority_queue))

        for p in range(0, 41, 2):
            priority_queue.enqueue(p * 2, p)

        list2 = [p * 2 for p in range(0, 41, 2)]

        for value in priority_queue:
            self.assertTrue(value in list2, "Wrong iterator implementation")
            self.assertEqual(value, max(list2))
            list2.remove(value)
        self.assertEqual(len(priority_queue), 0)
        self.assertTrue(priority_queue.size == 0)

        priority_queue = DuplicatePriorityQueue(elements_type=float, reverse=True)
        floats = [x/10 for x in range(3, 103, 5)]
        for x in floats:
            priority_queue.enqueue(x, int(x))

        self.assertEqual(list(iter(priority_queue)), floats, "Wrong iterator implementation")
        self.assertEqual(len(priority_queue), 0)
        self.assertTrue(priority_queue.size == 0)

    def test_peek(self):
        priority_queue = DuplicatePriorityQueue()
        self.assertTrue(priority_queue.peek() is None, "Wrong peek implementation")
        priority_queue = DuplicatePriorityQueue(float, True)
        self.assertTrue(priority_queue.peek() is None, "Wrong peek implementation")

        priority_queue.enqueue(15.25, 2)
        priority_queue.enqueue(10.13, 2)
        priority_queue.enqueue(423.56, 10)
        priority_queue.enqueue(20.02, 1)
        priority_queue.enqueue(20.02, 1)
        priority_queue.enqueue(33.5, 5)
        self.assertEqual(priority_queue.peek(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.peek(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.dequeue(), 20.02, "Wrong dequeue implementation")
        self.assertEqual(priority_queue.peek(), 15.25, "Wrong dequque implementation")
        self.assertEqual(priority_queue.dequeue(), 15.25, "Wrong dequque implementation")
        self.assertEqual(priority_queue.peek(), 10.13, "Wrong dequque implementation")
        self.assertEqual(len(priority_queue), 3)

    def test_get_element(self):
        priority_queue = DuplicatePriorityQueue()
        for k in range(10):
            self.assertTrue(priority_queue.get_element(k) is None, "Wrong get implementation")
            priority_queue.enqueue(k*3, k)
            priority_queue.enqueue(k**3, k)

        for n in range(9, -1, -1):
            self.assertEqual(priority_queue.get_element(n), n*3, "Wrong peek implementation")
            self.assertTrue(priority_queue.contains_element(n**3))

        self.assertEqual(len(priority_queue), 20)

    def test_replace_priority(self):
        priority_queue = DuplicatePriorityQueue(int, True)
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.replace_priority("element", 10.5)
        with self.assertRaises(PriorityQueueElementError):
            priority_queue.replace_priority(10, 5)
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.replace_priority(5, 5.5)

        priority_queue.enqueue(0, 10)
        priority_queue.enqueue(1, 1)
        priority_queue.enqueue(2, 2)
        priority_queue.enqueue(3, 5)

        with self.assertRaises(ValueError):
            priority_queue.replace_priority(3, 5, "comparison")

        self.assertEqual(priority_queue.peek(), 1)
        self.assertEqual(priority_queue.get_element(0), None)
        self.assertEqual(priority_queue.get_element(10), 0)
        self.assertTrue(priority_queue.replace_priority(0, 0, comparison=-1), "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(10), None, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(0), 0, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.peek(), 0, "Wrong replace_priority implementation")

        self.assertTrue(priority_queue.replace_priority(3, -1), "Wrong replace_priority implementation")
        self.assertFalse(priority_queue.replace_priority(3, -5, comparison=1), "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(5), None, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(-1), 3, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.peek(), 3, "Wrong replace_priority implementation")

        self.assertEqual(priority_queue.get_element(20), None)
        self.assertTrue(priority_queue.replace_priority(2, 20), "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(20), 2)

        priority_queue = DuplicatePriorityQueue()
        priority_queue.enqueue("str", 5)
        priority_queue.enqueue(5.5, 0)
        self.assertTrue(priority_queue.replace_priority("str", 10, comparison=1),
                        "Wrong replace_priority implementation")
        self.assertFalse(priority_queue.replace_priority("str", 12, comparison=-1),
                         "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(5), None)
        self.assertEqual(priority_queue.get_element(10), "str")
        self.assertEqual(priority_queue.peek(), "str")

        self.assertTrue(priority_queue.replace_priority(5.5, 10), "Wrong replace_priority implementation")
        self.assertEqual(len(priority_queue), 2, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.get_element(10), "str", "Wrong replace_priority implementation")

        priority_queue = DuplicatePriorityQueue(reverse=True)
        for i in range(1, 6):
            priority_queue.enqueue(i, i * 10)
        self.assertEqual(len(priority_queue), 5)
        self.assertTrue(priority_queue.replace_priority(2, 10), "Wrong replace_priority implementation")
        self.assertEqual(len(priority_queue), 5, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.dequeue(), 1, "Wrong replace_priority implementation")
        self.assertEqual(priority_queue.peek(), 2, "Wrong replace_priority implementation")

        for i in range(3, 6):
            self.assertTrue(priority_queue.replace_priority(i, 10), "Wrong replace_priority implementation")
        priority_queue.enqueue(0, 0)
        self.assertEqual(len(priority_queue), 5, "Wrong replace_priority implementation")
        self.assertEqual(list(iter(priority_queue)), [0, 2, 3, 4, 5], "Wrong replace_priority implementation")

    def test_remove(self):
        priority_queue = DuplicatePriorityQueue()
        with self.assertRaises(PriorityQueueElementError):
            priority_queue.remove_element(5)

        priority_queue.enqueue("word", 1)
        priority_queue.enqueue(1, 5)
        priority_queue.enqueue(3.14, 10)
        priority_queue.remove_element(3.14)
        self.assertFalse(priority_queue.contains_element(3.14), "Wrong remove implementation")
        self.assertEqual(priority_queue.peek(), 1, "Wrong remove implementation")
        with self.assertRaises(PriorityQueueElementError):
            priority_queue.remove_element(3.14)
        self.assertEqual(priority_queue.size, 2, "Wrong remove implementation")

        priority_queue = DuplicatePriorityQueue(int, reverse=True)
        with self.assertRaises(PriorityQueueTypeError):
            priority_queue.remove_element(5.5)

        for i in range(10):
            priority_queue.enqueue(i, i**2)
            priority_queue.enqueue(i + 100, i**2)
        self.assertEqual(len(priority_queue), 20)
        self.assertTrue(priority_queue.contains_element(5))
        priority_queue.remove_element(5)
        self.assertEqual(len(priority_queue), 19, "Wrong remove implementation")
        self.assertFalse(priority_queue.contains_element(5), "Wrong remove implementation")

        priority_queue.remove_element(0)
        self.assertEqual(priority_queue.dequeue(), 100, "Wrong remove implementation")

        self.assertTrue(priority_queue.contains_priority(9))
        self.assertTrue(3 in priority_queue)
        self.assertTrue(103 in priority_queue)

        priority_queue.remove_element(3)

        self.assertTrue(priority_queue.contains_priority(9))
        self.assertFalse(3 in priority_queue)
        self.assertTrue(103 in priority_queue)

        self.assertEqual(priority_queue.get_element(9), 103, "Wrong remove implementation")
        priority_queue.remove_element(103)
        self.assertFalse(priority_queue.contains_priority(9), "Wrong remove implementation")
        self.assertEqual(len(priority_queue), 15, "Wrong remove implementation")

        self.assertEqual(priority_queue.dequeue(), 1)
        priority_queue.remove_element(101)
        self.assertEqual(priority_queue.get_element(1), None, "Wrong remove implementation")
        self.assertEqual(len(priority_queue), 13)


if __name__ == "__main__":
    unittest.main()
