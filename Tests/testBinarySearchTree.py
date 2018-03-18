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


# Simple unittests for the ADT BinarySearchTree
import unittest

from ADTs.TreeDataStructures import BinarySearchTree
from ADTs.BinarySearchTreeErrors import *


class BinarySearchTreeTest(unittest.TestCase):

    def test_size(self):
        binary = BinarySearchTree(12)
        self.assertEqual(binary.get_number_of_elements(), len(binary), "Len method not working.")
        self.assertEqual(binary.get_number_of_elements(), 1, "The binary tree must be with 1 elements when initialised"
                                                             "with a root.")
        binary = BinarySearchTree()
        self.assertEqual(binary.get_number_of_elements(), 0, "The binary tree must be with 0 elements when initialised")
        binary.add(25)
        for i in range(1, 11):
            binary.add(i)
            binary.add(i + 25)
            self.assertEqual(binary.get_number_of_elements(), len(binary), "Len method not working.")
        self.assertEqual(binary.get_number_of_elements(), 21, "BinaryTree gives wrong size.")

    def test_contains(self):
        binary = BinarySearchTree(26)
        binary.add(12)
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.contains(12.50)
        binary.add(54)
        self.assertTrue(binary.contains(12), "BinaryTree contain method doesn't work.")
        binary.add(32)
        self.assertFalse(binary.contains(104), "BinaryTree contain method doesn't work.")
        binary.add(104)
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.contains("string")
        binary.add(0)
        self.assertTrue(binary.contains(26), "BinaryTree contain method doesn't work.")
        binary.add(5)
        self.assertTrue(binary.contains(5), "BinaryTree contain method doesn't work.")
        self.assertTrue(binary.contains(0), "BinaryTree contain method doesn't work.")

    def test_add(self):
        binary = BinarySearchTree()
        binary.add(23)
        self.assertEqual(binary.get_root(), 23, "Add method cannot add the item to the root")
        self.assertEqual(binary.get_number_of_elements(), 1, "Add method doesn't increment number of elements")
        binary.add(12)
        binary.add(54)
        binary.add(1)
        self.assertEqual(binary.get_number_of_elements(), 4, "Add method doesn't adjust the number of elements")
        self.assertTrue(binary.contains(54), "Add method doesn't add the elements properly")
        self.assertFalse(binary.contains(0), "Add method adds elements that are not supposed to be there.")
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.add("string")
        binary.add(23)
        self.assertEqual(binary.get_number_of_elements(), 4, "Add method adds elements which already exist.")

    def test_delete(self):
        binary = BinarySearchTree()
        with self.assertRaises(EmptyBinarySearchTreeError):
            binary.delete(1)

        binary = BinarySearchTree(50)
        binary.delete(50)
        self.assertEqual(binary.get_number_of_elements(), 0, "Delete method cannot delete the root.")
        self.assertFalse(binary.contains(50), "Delete method cannot delete the root")
        binary.add(1)
        binary.add(0)
        binary.add(2)
        binary.add(3)
        binary.delete(2)
        self.assertEqual(binary.get_number_of_elements(), 3, "Delete method cannot delete properly.")
        binary.add(12)
        binary.add(9)
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.delete("9")
        binary.add(34)
        binary.delete(1)
        self.assertEqual(binary.get_number_of_elements(), 5, "Delete method cannot delete the root.")
        self.assertFalse(binary.contains(1), "Delete method cannot delete the root")
        binary.add(-4)
        binary.add(-6)
        binary.delete(-4)
        self.assertEqual(binary.get_number_of_elements(), 6, "Delete method cannot delete a node with one child.")
        self.assertFalse(binary.contains(-4), "Delete method cannot a node with one child.")
        with self.assertRaises(BinarySearchTreeElementError):
            binary.delete(11232)

    def test_iterator(self):
        numbers = [30, 22, 46, 11, 15, 26, 101, 67, 140, 38]
        binary = BinarySearchTree()
        for number in numbers:
            binary.add(number)
        index = 0
        numbers.sort()
        for number in binary:
            self.assertEqual(number, numbers[index], "Iterator doesn't return correct values")
            index += 1

        binary = BinarySearchTree()
        count = 0
        for i in binary:
            count += i
        self.assertEqual(count, 0, "Iterator doesn't work with empty tree")

    def test_type(self):
        with self.assertRaises(BinarySearchTreeTypeError):
            BinarySearchTree(elements_type=None)

        with self.assertRaises(BinarySearchTreeTypeError):
            BinarySearchTree(elements_type=2)

        binary = BinarySearchTree(elements_type=str)
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.add(4)
        with self.assertRaises(BinarySearchTreeTypeError):
            BinarySearchTree(root="hey", elements_type=int)

        binary = BinarySearchTree(root="hey", elements_type=str)
        words = ["hey", "abc", "zcd", "dfg", "cxz", "xsa", "gfd", "word", "anotherword"]
        counter = 0
        for word in words:
            binary.add(word)
            with self.assertRaises(BinarySearchTreeTypeError):
                binary.add(counter)
            counter += 1
            self.assertEqual(len(binary), counter, "Len method of the binary tree doesn't work")
        self.assertTrue(binary.contains("abc"), "Contains method doesn't work with strings")
        self.assertFalse(binary.contains("hbh"), "Contains method doesn't work with strings")
        self.assertEqual(binary.get_minimum(), "abc", "Binary tree doesn't return minimum element.")
        self.assertEqual(binary.get_maximum(), "zcd", "Binary tree doesn't return maximum element.")

        words.sort()
        index = 0
        for word in binary:
            self.assertEqual(word, words[index], "Iterator doesn't work with strings")
            index += 1

        with self.assertRaises(BinarySearchTreeTypeError):
            binary.delete(index)
        with self.assertRaises(BinarySearchTreeTypeError):
            binary.delete([])

        binary.delete("abc")
        self.assertEqual(binary.get_minimum(), "anotherword", "Binary tree delete method doesn't work properly")

        with self.assertRaises(BinarySearchTreeElementError):
            binary.delete("gfgfg")

        self.assertTrue(binary.get_root() == "hey", "Binary tree get_root method doesn't work properly")
        binary.delete("hey")
        self.assertTrue(binary.get_root() != "hey", "Binary tree delete method doesn't work properly")

        binary = BinarySearchTree()
        self.assertTrue(binary.get_root() is None, "Binary tree get_root method doesn't work properly")
        binary.add(1)
        binary.delete(1)
        self.assertTrue(binary.get_root() is None, "Binary tree get_root method doesn't work properly after deletion")

    def test_get_min(self):
        binary = BinarySearchTree(elements_type=int)
        self.assertEqual(binary.get_minimum(), None, "Incorrect implementation of get_min")

        binary = BinarySearchTree(root=5)
        self.assertEqual(binary.get_minimum(), 5, "Incorrect implementation of get_min")

        binary = BinarySearchTree(root=10)
        binary.add(11)
        binary.add(5)
        binary.add(223)
        self.assertEqual(binary.get_minimum(), 5, "Incorrect implementation of get_min")

        binary = BinarySearchTree(root=2.5, elements_type=float)
        l_test = [2.4, 5.7, 3.3, 7.8, 8.99]
        for i in l_test:
            binary.add(i)
        self.assertEqual(binary.get_minimum(), min(l_test))

    def test_get_max(self):
        binary = BinarySearchTree(elements_type=int)
        self.assertEqual(binary.get_maximum(), None, "Incorrect implementation of get_max")

        binary = BinarySearchTree(root=5)
        self.assertEqual(binary.get_maximum(), 5, "Incorrect implementation of get_max")

        binary = BinarySearchTree(root=10)
        binary.add(11)
        binary.add(5)
        binary.add(223)
        self.assertEqual(binary.get_maximum(), 223, "Incorrect implementation of get_max")

        binary = BinarySearchTree(root=2.5, elements_type=float)
        l_test = [2.4, 5.7, 3.3, 7.8, 8.99]
        for i in l_test:
            binary.add(i)
        self.assertEqual(binary.get_maximum(), max(l_test))

    def test_str(self):
        binary = BinarySearchTree()
        self.assertEqual(str(binary), "Binary search tree with root: None")

        binary = BinarySearchTree(5)
        self.assertEqual(str(binary), "Binary search tree with root: 5")

        binary = BinarySearchTree("root", elements_type=str)
        self.assertEqual(str(binary), "Binary search tree with root: root")


if __name__ == '__main__':
    unittest.main()
