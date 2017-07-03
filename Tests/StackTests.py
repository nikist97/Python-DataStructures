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

        stack = Stack(str)
        self.assertEqual(stack.size(), 0, "Stack size should be 0 at initialization")
        for l in ["a", "d", "b", "m"]:
            stack.push(l)

        stack.pop()
        self.assertEqual(stack.size(), 3, "Incorrect stack size")

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty(), "Stack should be empty")
        stack.push("word")
        stack.push("sentence")
        stack.pop()
        self.assertFalse(stack.is_empty(), "Stack should not be empty")

        stack = Stack(int)
        self.assertTrue(stack.is_empty(), "Stack should be empty")

        stack.push(0)
        self.assertFalse(stack.is_empty(), "Stack should not be empty")

    def test_peek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None, "Top element of stack should be None at initialization")
        stack.push(2)
        stack.push("Tests")
        self.assertEqual(stack.peek(), "Tests", "Stack gives wrong peek")

        stack = Stack(float)
        self.assertEqual(stack.peek(), None, "Top element of stack should be None at initialization")
        stack.push(3.5)
        stack.push(1.27)
        stack.push(2.0)
        self.assertEqual(stack.peek(), 2.0, "Stack gives wrong peek")

    def test_pop(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.pop()
        stack.push([1, 2, 3])
        self.assertEqual(stack.pop()[1], 2, "Stack pops wrong element")
        stack.push("pushed string")
        self.assertEqual(stack.pop(), "pushed string", "Stack pops wrong element")

        stack = Stack(bool)
        with self.assertRaises(ValueError):
            stack.pop()
        stack.push(True)
        stack.push(False)
        stack.pop()
        self.assertTrue(stack.pop(), "Stack pops wrong element")

    def test_push(self):
        stack = Stack()
        stack.push(23)
        stack.push(20)
        self.assertEqual(stack.peek(), 20, "Wrong stack push implementation")
        self.assertEqual(len(stack), 2, "Wrong stack push implementation")

        stack = Stack(bool)
        with self.assertRaises(TypeError):
            stack.push("word")

        for i in range(10):
            if i % 2 == 0:
                stack.push(True)
            else:
                stack.push(False)
        self.assertEqual(stack.size(), 10, "Wrong stack push implementation")

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

    def test_str(self):
        stack = Stack(int)
        self.assertEqual(str(stack), "[]", "String representation of stack doesn't work with empty stacks")

        stack.push(0)
        self.assertEqual(str(stack), "[0]", "String representation of stack doesn't work with singleton stacks")

        for i in [5, 20, 11, 34, 2]:
            stack.push(i)

        self.assertEqual(str(stack), "[0, 5, 20, 11, 34, 2]",
                         "String representation of stack doesn't work with many elements")

        stack.peek()
        stack.pop()
        stack.pop()
        self.assertEqual(str(stack), "[0, 5, 20, 11]",
                         "String representation of stack doesn't work after pop and peek operations")

        stack = Stack()
        stack.push(2.5)
        stack.push(0)
        self.assertEqual(str(stack), "[2.5, 0]")

    def test_iterator(self):
        stack = Stack(int)

        for i in range(20, 42, 2):
            stack.push(i)

        integers = list(range(20, 42, 2))
        self.assertEqual(len(stack), len(integers), "Size method doesn't work")

        index = len(integers) - 1
        for num in stack:
            self.assertEqual(num, integers[index], "Iterator doesn't work")
            index -= 1

        self.assertEqual(len(stack), 0, "iterator doesn't adjust stack size")

    def test_contains(self):
        stack = Stack()
        self.assertFalse(1 in stack, "Stack contains method doesn't work")

        stack.push("word")
        self.assertEqual("word" in stack, stack.contains("word"), "Stack contains method doesn't work")
        self.assertTrue(stack.contains("word"), "Stack contains method doesn't work")

        stack = Stack(elements_type=float)
        stack.push(1.55)
        stack.push(2.3)
        self.assertTrue(2.3 in stack, "Stack contains method doesn't work")
        self.assertTrue(stack.contains(1.55), "Stack contains method doesn't work")

        with self.assertRaises(TypeError):
            boolean = 4 in stack

        with self.assertRaises(TypeError):
            boolean = stack.contains("word")

if __name__ == '__main__':
    unittest.main()
