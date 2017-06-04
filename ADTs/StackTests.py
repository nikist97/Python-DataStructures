# Simple unittests for the ADT Stack
import unittest

from ADTs.AbstractDataStructures import Stack


class StackTest(unittest.TestCase):

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0, "Stack size should be 0 at initialization")
        for i in range(1, 41):
            stack.push(i)
            stack.push(i+1)
            stack.pop()
        self.assertEqual(stack.size(), 40, "Incorrect stack size")

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty(), "Stack should be empty")
        stack.push("word")
        stack.push("sentence")
        stack.pop()
        self.assertFalse(stack.is_empty(), "Stack should not be empty")

    def test_peek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None, "Top element of stack should be None at initialization")
        stack.push(2)
        stack.push("test")
        self.assertEqual(stack.peek(), "test", "Stack gives wrong peek")

    def test_pop(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.pop()
        stack.push([1, 2, 3])
        self.assertEqual(stack.pop()[1], 2, "Stack pops wrong element")
        stack.push("pushed string")
        self.assertEqual(stack.pop(), "pushed string", "Stack pops wrong element")

    def test_type(self):
        stack = Stack()
        self.assertEqual(stack.type(), None)

        stack = Stack(elements_type=list)
        self.assertEqual(stack.type(), list)

        with self.assertRaises(TypeError):
            stack.push("hey")

        stack = Stack(elements_type=str)
        stack.push("world")
        stack.push("hello")
        test_string = stack.pop() + " " + stack.pop()
        self.assertEqual(test_string, "hello world", "Stack with strings doesn't pop correctly")

        with self.assertRaises(TypeError):
            stack.push(123)

if __name__ == '__main__':
    unittest.main()
