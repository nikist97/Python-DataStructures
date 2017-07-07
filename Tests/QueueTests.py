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


# Simple unittests for the ADT Queue
import unittest

from ADTs.AbstractDataStructures import Queue


class QueueTest(unittest.TestCase):

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0, "Queue size should be 0 at initialization")
        for i in range(1, 41):
            queue.enqueue(i)
            queue.enqueue(i + 1)
            queue.dequeue()
        self.assertEqual(queue.size(), 40, "Incorrect queue size")

        queue = Queue(str)
        self.assertEqual(queue.size(), 0, "Queue size should be 0 at initialization")
        queue.enqueue("b")
        self.assertEqual(queue.size(), 1, "Incorrect queue size")
        queue.enqueue("c")
        queue.peek()
        self.assertEqual(queue.size(), 2, "Incorrect queue size")

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), "[]", "Wrong str representation")

        queue.enqueue(1)
        queue.enqueue(2.5)
        self.assertEqual(str(queue), "[1, 2.5]", "Wrong str representation")

        queue = Queue(int)
        self.assertEqual(str(queue), "[]", "Wrong str representation")
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(str(queue), "[0, 1, 2, 3, 4]", "Wrong str representation")

    def test_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty(), "Queue should be empty")
        queue.enqueue("word")
        queue.enqueue("sentence")
        queue.dequeue()
        self.assertFalse(queue.is_empty(), "Queue should not be empty")

        queue = Queue(float)
        self.assertTrue(queue.is_empty(), "Queue should be empty")
        queue.enqueue(2.5)
        queue.peek()
        queue.enqueue(1.54)
        queue.dequeue()
        self.assertFalse(queue.is_empty(), "Queue should not be empty")

    def test_peek(self):
        queue = Queue()
        self.assertEqual(queue.peek(), None, "Top element of queue should be None at initialization")
        queue.enqueue(2)
        queue.enqueue("Tests")
        self.assertEqual(queue.peek(), 2, "Queue gives wrong peek")

        queue = Queue(int)
        self.assertEqual(queue.peek(), None, "Top element of queue should be None at initialization")
        queue.enqueue(23)
        self.assertEqual(queue.peek(), 23, "Queue gives wrong peek")
        queue.dequeue()
        queue.enqueue(57)
        queue.enqueue(0)
        self.assertEqual(queue.peek(), 57, "Queue gives wrong peek")

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue([1, 2, 3])
        queue.enqueue("item")
        self.assertEqual(queue.dequeue()[1], 2, "Queue dequeues wrong element")
        self.assertEqual(len(queue), 1, "Wrong enqueue implementation")

        queue = Queue(str)
        with self.assertRaises(TypeError):
            queue.enqueue(5)
        self.assertEqual(len(queue), 0)
        self.assertTrue(queue.is_empty())

        queue.enqueue("2")
        queue.enqueue("word")
        self.assertEqual(len(queue), 2, "Wrong enqueue implementation")
        self.assertFalse(queue.is_empty(), "Wrong enqueue implementation")
        self.assertEqual(queue.dequeue(), "2", "Wrong enqueue implementation")

    def test_dequeue(self):
        queue = Queue()
        with self.assertRaises(ValueError):
            queue.dequeue()

        queue.enqueue(4)
        queue.enqueue("word")
        self.assertEqual(queue.dequeue(), 4, "Wrong queue implementation")

        queue = Queue(tuple)
        with self.assertRaises(ValueError):
            queue.dequeue()

        queue.enqueue((2,))
        queue.enqueue((1, 2, 3))
        self.assertEqual(queue.dequeue()[0], 2, "Wrong dequeue implementation")

    def test_type(self):
        queue = Queue()
        self.assertEqual(queue.type(), None)

        queue = Queue(elements_type=list)
        self.assertEqual(queue.type(), list)

        with self.assertRaises(TypeError):
            queue.enqueue("hey")

        queue = Queue(elements_type=str)
        queue.enqueue("hello")
        queue.enqueue("world")
        test_string = queue.dequeue() + " " + queue.dequeue()
        self.assertEqual(test_string, "hello world", "Queue with strings doesn't dequeue correctly")

        with self.assertRaises(TypeError):
            queue.enqueue(123)

    def test_contains(self):
        queue = Queue()
        self.assertFalse(0 in queue, "Wrong contains implementation")

        queue.enqueue(1)
        queue.enqueue(10)
        self.assertEqual(10 in queue, queue.contains(10))
        self.assertTrue(10 in queue, "Wrong contains implementation")

        queue = Queue(float)
        queue.enqueue(2.3)
        queue.enqueue(3.7)
        queue.dequeue()
        queue.peek()
        self.assertTrue(3.7 in queue)
        self.assertFalse(2.3 in queue)

    def test_iterator(self):
        queue = Queue(str)
        words = ["word", "python", "java", "csharp"]
        index = 0

        for word in queue:
            self.assertEqual(word, words[index], "Wrong iterator implementation")
            index += 1

        self.assertEqual(len(queue), 0)

if __name__ == '__main__':
    unittest.main()
