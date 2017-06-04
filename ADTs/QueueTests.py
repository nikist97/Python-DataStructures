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

    def test_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty(), "Queue should be empty")
        queue.enqueue("word")
        queue.enqueue("sentence")
        queue.dequeue()
        self.assertFalse(queue.is_empty(), "Queue should not be empty")

    def test_peek(self):
        queue = Queue()
        self.assertEqual(queue.peek(), None, "Top element of queue should be None at initialization")
        queue.enqueue(2)
        queue.enqueue("test")
        self.assertEqual(queue.peek(), 2, "Queue gives wrong peek")

    def test_enqueue(self):
        queue = Queue()
        with self.assertRaises(ValueError):
            queue.dequeue()
        queue.enqueue([1, 2, 3])
        queue.enqueue("item")
        self.assertEqual(queue.dequeue()[1], 2, "Queue dequeues wrong element")

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

if __name__ == '__main__':
    unittest.main()
