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


from abc import ABC, abstractmethod
from copy import deepcopy


class Stack(object):
    """
    Implementation for the abstract data structure called Stack - follows the principle Last In First Out
    """

    def __init__(self, elements_type=None):
        """
        a constructor for a stack
        :param elements_type: optional argument, which represents the type of data in the stack (int, str, float, etc.)
             default value is None, which means that the stack can contain elements of all types,
             otherwise, it can contain only elements of the specified type
        """

        # checking that the elements_type argument is a valid type if passed
        if elements_type is not None and type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        # the elements in the stack are stored in a python list
        self.__elements = []
        self.__elements_type = elements_type

    def __str__(self):
        """
        the string representation for the stack returns the string representation of the list of
        elements in the stack
        """

        return str(self.__elements)

    def __len__(self):
        """
        overriding this method lets us use the len(stack) syntax, where stack is an object of type Stack
        :return: calls the size() method of the stack to get the number of elements in the stack
        """

        return self.size()

    def __iter__(self):
        """
        overriding this method allows the use of an iterator for a Stack object
        :return: returns a reference to the object itself
        """

        return self

    def __next__(self):
        """
        overriding this method impements the next() method of the iterator so that the Stack object is iterable
        :return: calls the pop() method to return the appropriate element and remove it from the stack
        :raises StopIteration: if the stack is empty
        """

        if self.is_empty():
            raise StopIteration
        else:
            return self.pop()

    def __contains__(self, item):
        """
        overriding this method allows the use of the 'item in stack' syntax, where 'item' is some value, while stack
        is an object of type Stack
        :param item: the value to search for in the stack
        :return: calls the contains() method to check if the stack contains this value
        """

        return self.contains(item)

    def contains(self, item):
        """
        this method checks if a value is contained in the stack
        :param item: the value to search for in the stack
        :return: True if the value is contained in the list with elements of the stack and False otherwise
        :raises TypeError: if the type of the Stack object is specified and is different from the type of the 'item'
            argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            return item in self.__elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elements_type))

    def is_empty(self):
        """
        this method checks if the stack is empty
        :return: True if the number of elements in the stack is 0 and False otherwise
        """

        return self.size() == 0

    def size(self):
        """
        this method gets the number of elements in the stack
        :return: the number of elements in the list containing the elements of the stack
        """

        return len(self.__elements)

    def type(self):
        """
        this method gets the type of elements in the stack
        :return: the type of elements in the stack or None if there are elements of multiple types in the stack
        """

        return self.__elements_type

    def push(self, item):
        """
        this method pushes an element on top of the stack
        :param item: the element to push in the stack
        :raises TypeError: if the type of the Stack object is specified and is different from the type of the 'item'
            argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            self.__elements.append(item)
        else:
            raise TypeError("The element you are trying to push is not of type " + str(self.__elements_type))

    def pop(self):
        """
        this method pops the top element out of the stack (the last pushed element in the stack)
        :return: the top element in the stack
        :raises ValueError: if there are no elements in the stack
        """

        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            raise ValueError("There are no elements in the stack")

    def peek(self):
        """
        this method peeks the top element of the stack, same as the pop() method,
        but without removing the element from the stack
        :return: the last pushed element in the stack or None if there are no elements in the stack
        """

        if len(self.__elements) > 0:
            return self.__elements[len(self.__elements) - 1]
        else:
            return None

    def remove(self, element):
        """
        this method removes an element from the stack
        :param element: the element to remove from the stack
        :raises TypeError: if the type of the Stack object is specified and is different from the type of the 'element'
            argument used when calling this method
        :raises KeyError: if the element to remove is not contained in the stack
        """

        if self.__elements_type is None or type(element) == self.__elements_type:
            try:
                self.__elements.remove(element)
            except ValueError:
                raise KeyError("The element you are trying to remove is not contained in the stack")
        else:
            raise TypeError("The element you are trying to remove is not of type " + str(self.__elements_type))


class Queue(object):
    """
    Implementation for the abstract data structure called Queue - follows the principle First In First Out
    """

    def __init__(self, elements_type=None):
        """
        a constructor for a Queue
        :param elements_type: optional argument, which represents the type of elements in the queue
            default value is None, which means that the queue can contain elements of all types,
            otherwise, the queue can only contain elements of the specified type
        :raises TypeError: if the 'elements_type' argument is specified and is not a valid type
        """

        # checking that the elements_type argument is a valid type if passed
        if elements_type is not None and type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        # the elements in the queue are spread among two stacks in order to ensure better amortized time complexity cost
        # for the dequeue() method
        self.__in_elements = Stack(elements_type)
        self.__out_elements = Stack(elements_type)
        self.__elements_type = elements_type

    def __str__(self):
        """
        the string representation of a queue object
        :return: the elements in teh stack in the order they must be dequeued
        """

        # noinspection PyProtectedMember
        return str(self.__out_elements._Stack__elements[:: -1] + self.__in_elements._Stack__elements)

    def __len__(self):
        """
        overriding this method allows the use of the len(queue) syntax, where queue is an object of type Queue
        :return: calls the size() method to get the number of elements in the queue
        """

        return self.size()

    def __iter__(self):
        """
        overriding this method allows the use of an iterator for the queue
        :return: reference to the queue object itself
        """

        return self

    def __next__(self):
        """
        overriding this method implements the next method for the iterator
        :return: calls the dequeue() method to get the appropriate value to return and remove it from the queue
        :raises StopIteration: if there are no elements in the queue
        """

        if self.is_empty():
            raise StopIteration
        else:
            return self.dequeue()

    def __contains__(self, item):
        """
        overriding this method allows the use of the 'item in queue' syntax, where the queue object is of type Queue
        :param item: the item to search for in the queue
        :return: calls the contains() method to check if the item is contained in the queue
        """

        return self.contains(item)

    def contains(self, item):
        """
        this method checks if an item is contained in the queue
        :param item: the item to search for in the queue
        :return: True if the item is contained in the queue and False otherwise
        :raises TypeError: if the queue has a type of elements specified that is different from the type of the 'item'
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            return item in self.__out_elements or item in self.__in_elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elements_type))

    def is_empty(self):
        """
        this method checks if the queue is empty
        :return: True if the number of elements in the queue is 0 and False otherwise
        """

        return self.size() == 0

    def size(self):
        """
        this method gets the number of elements in the queue
        :return: the number of elements in the queue
        """

        return len(self.__out_elements) + len(self.__in_elements)

    def type(self):
        """
        this method gets the type of elements in the queue
        :return: the type of elements in the queue or None if the queue can contain all types of elements
        """

        return self.__elements_type

    def enqueue(self, item):
        """
        this method enqueues an element in the queue
        :param item: the element to enqueue
        :raises TypeError: if the type of elements in the queue is specified and is different from the type
            of the 'item' argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            self.__in_elements.push(item)
        else:
            raise TypeError("The element you are trying to enqueue is not of type " + str(self.__elements_type))

    def dequeue(self):
        """
        this method removes the item that got first in the queue
        :raises ValueError: if there are no elements in the queue
        """

        if self.size() > 0:
            # if the stack for handling the dequeue operation is empty, fill it up with the elements in the stack
            # for handling the enqueue operation
            if self.__out_elements.is_empty():
                while not self.__in_elements.is_empty():
                    self.__out_elements.push(self.__in_elements.pop())
            return self.__out_elements.pop()
        else:
            raise ValueError("There are no elements in the queue")

    def peek(self):
        """
        this method peeks the item that got first in the queue (without removing it)
        :return: the peeked item or None if there are no elements in the queue
        """

        if self.size() > 0:
            # if the stack for handling the dequeue operation is empty, fill it up with the elements in the stack
            # for handling the enqueue operation
            if self.__out_elements.is_empty():
                while not self.__in_elements.is_empty():
                    self.__out_elements.push(self.__in_elements.pop())
            return self.__out_elements.peek()
        else:
            return None

    def remove(self, element):
        """
        this method removes an element from the queue
        :param element: the element to remove from the queue
        :raises TypeError: if the type of elements in the queue is specified and is different from the type
            of the 'element' argument used when calling this method
        :raises KeyError: if the element to remove is not contained in the queue
        """

        if self.__elements_type is None or type(element) == self.__elements_type:
            try:
                self.__in_elements.remove(element)
            except KeyError:
                try:
                    self.__out_elements.remove(element)
                except KeyError:
                    raise KeyError("The element you are trying to remove is not contained in the queue")
        else:
            raise TypeError("The element you are trying to remove is not of type " + str(self.__elements_type))


class BinarySearchTree(object):
    """
    implementation for the Abstract Data Structure called Binary Search Tree
    """

    def __init__(self, root=None, elements_type=int):
        """
        constructor for a binary search tree
        :param root: optional argument, which represents the value of the root node of the binary search tree,
            default value is None, tree initialised with no root
        :param elements_type: optional argument, the type of elements in the binary search tree,
            default value is int, the argument must be a valid type, only elements of this type are allowed in the tree
        :raises TypeError: if the 'elements_type' argument is not a valid type (int, str, float, etc.)
        :raises TypeError: if a root is specified and its type is different from the type of the binary search tree
        """

        # variables used for the iterator of the binary tree
        self.__successor = None
        self.__iterator_limit = None
        self.__iterator_finished = None
        self.__current_item = None

        # check for a valid type
        if type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        # initialising the binary search tree
        self.__elements_type = elements_type

        if root is None:
            self.__root = root
            self.__number_of_items = 0
        elif root is not None and type(root) == elements_type:
            self.__root = Node(root)
            self.__number_of_items = 1
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(elements_type) + ".")

    def __str__(self):
        """
        the string representation of the binary search tree
        :return: returns a string, which contains information about the tree, such as the root value
        """

        if self.__root is not None:
            return "Binary search tree with root: " + str(self.__root.get_value())
        else:
            return "Binary search tree with root: None"

    def __contains__(self, item):
        """
        overriding this method allows the use of the 'item in tree' syntax where tree is an object of type
        BinarySearchTree
        :param item: the item to search for in the tree
        :return: calls the contains() method to check if the tree contains the item
        """

        return self.contains(item)

    def __len__(self):
        """
        overriding this method allows the use of the 'len(tree)' syntax where tree is an object of type
        BinarySearchTree
        :return: calls the get_number_of_elements() method to get the number of elements in the tree
        """

        return self.get_number_of_elements()

    def is_empty(self):
        """
        this method checks if the tree has no elements
        :return: True if the number of elements in the tree is 0 and False otherwise
        """

        return self.get_number_of_elements() == 0

    def __iter__(self):
        """
        overriding this method allows the implementation of an iterator for the tree
        :return: a reference to the tree itself
        """

        # setting the instance variables used for the iteration
        self.__current_item = self.__get_minimum_node()
        self.__successor = self.__current_item
        self.__iterator_limit = self.__get_maximum_node()
        self.__iterator_finished = False
        return self

    def __next__(self):
        """
        overriding this method to implement the next() method for the iterator
        :return: the next item to iterate
        :raises StopIteration: if the iteration is over
        """

        if self.__iterator_finished:
            raise StopIteration

        else:
            # assigning the current_item, which will be returned, to its successor
            self.__current_item = self.__successor

            # if there is no successor, raise StopIteration
            if self.__current_item is None:
                raise StopIteration

            # if the current item has reached the iterator limit, which is the maximum element of the binary tree
            # return the current item's value and adjust the state of the iterator
            if self.__current_item.get_value() == self.__iterator_limit.get_value():
                self.__iterator_finished = True
                return self.__current_item.get_value()

            # else find the successor of the current item and return the current item's value
            else:
                # if the current item has a right child, go right and then go left as much as possible
                if self.__current_item.get_right() is not None:
                    self.__successor = self.__current_item.get_right()
                    while self.__successor.get_left() is not None:
                        self.__successor = self.__successor.get_left()

                # else if there is no right child, go up left as much as possible and then go right
                else:
                    while self.__successor.get_parent().get_right() == self.__successor:
                        self.__successor = self.__successor.get_parent()
                    self.__successor = self.__successor.get_parent()

                return self.__current_item.get_value()

    def add(self, value):
        """
        this method adds a new element to the tree
        :param value: the value of the new node to add
        :raises TypeError: if the type of the argument is different than the type of elements in the binary search tree
        """

        if type(value) == self.__elements_type:
            # if there is no root, create one
            if self.__root is None or self.__root.get_value() is None:
                self.__root = Node(value)
                self.__number_of_items = 1
            else:
                # if there is a root created, call the add method to the Node root object
                if self.__root.add(Node(value)):
                    self.__number_of_items += 1
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    def contains(self, value):
        """
        this method checks if an element with a certain value exists in the tree
        :param value: the value to search for in the tree
        :return: True if the tree contains an element with this value and False otherwise
        :raises TypeError: if the type of the argument is different than the type of elements in the binary search tree
        """

        if type(value) == self.__elements_type:
            return self.__root.contains(value)
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    def delete(self, value):
        """
        this method deletes an element with a certain value from the tree
        :param value: the value to delete
        :raises TypeError: if the type of the argument is different than the type of elements in the binary search tree
        """

        if type(value) == self.__elements_type:
            self.__root.delete(value)
            self.__number_of_items -= 1
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    def get_root(self):
        """
        this method gets the value of the root of the tree
        :return: the value of the root of the tree and None if there is no root
        """

        if self.__root is None:
            return None
        else:
            return self.__root.get_value()

    def get_number_of_elements(self):
        """
        this method gets the number of elements in the tree
        :return: the number of items
        """

        return self.__number_of_items

    def type(self):
        """
        get the type of elements in the tree
        :return: the type of elements in the tree (int, str, float, etc.)
        """

        return self.__elements_type

    def get_minimum(self):
        """
        a getter method for the element with the minimum value in the tree
        :return: the most left node's value or None if there is no root in the tree
        """

        current_node = self.__root

        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node.get_value()

    def __get_minimum_node(self):
        """
        a 'private' method intended to be used by the iterator of the tree
        :return: the most left node object in the tree (returns the Node object itself not its value)
        """

        current_node = self.__root

        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node

    def get_maximum(self):
        """
        a getter method for the element with the maximum value in the tree
        :return: the right most node's value or None if there is no root in the tree
        """

        current_node = self.__root

        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node.get_value()

    def __get_maximum_node(self):
        """
        a 'private' method intended to be used by the iterator of the tree
        :return: the most right node object in the tree (returns the Node object itself not its value)
        """

        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node


class Node(object):
    """
    a utility class, which represents a Node in the binary search tree
    """

    def __init__(self, value):
        """
        a constructor for the Node class, a node object has a value, a parent node, left and right child nodes
        :param value: the value of the node
        """

        self.__value = value
        self.__left = None
        self.__right = None
        self.__parent = None

    def get_value(self):
        """
        a getter method for the value of the node
        :return: the value of the node
        """

        return self.__value

    def get_left(self):
        """
        a getter method for the left child
        :return: the left child node of this node
        """

        return self.__left

    def set_left(self, node=None):
        """
        a setter method for the left child of this node
        :param node: (optional) the new node object to set to be the left child, default value is None (no left child)
        :raises TypeError: if the type of the argument is not Node
        """

        if node is None or type(node) == Node:
            self.__left = node
        else:
            raise TypeError("The child of a node must be a node.")

    def get_right(self):
        """
        a getter method for the right child
        :return: the right child node of this node
        """

        return self.__right

    def set_right(self, node=None):
        """
        a setter method for the right child of this node
        :param node: (optional) the new node object to set to be the right child, default value is None (no right child)
        :raises TypeError: if the type of the argument is not Node
        """

        if node is None or type(node) == Node:
            self.__right = node
        else:
            raise TypeError("The child of a node must be a node.")

    def get_parent(self):
        """
        a getter method for the parent
        :return: the parent node of this node
        """

        return self.__parent

    def set_parent(self, node=None):
        """
        a setter method for the parent of this node
        :param node: (optional) the new node object to set to be the parent, default value is None (no parent)
        :raises TypeError: if the type of the argument is not Node
        """

        if node is None or type(node) == Node:
            self.__parent = node
        else:
            raise TypeError("The parent of a node must be a node.")

    def add(self, node):
        """
        this method adds a node to the current node as a child by determining the right place of the node
        :param node: the node to add
        :return: True if the element has been added and False otherwise
        :raises TypeError: if the type of the argument is not Node
        """

        if type(node) == Node:
            # if the node's value is less than the current node's value, go to the left subtree
            if node.get_value() < self.get_value():
                if self.__left is None:
                    self.__add_left(node)
                    return True
                else:
                    return self.__left.add(node)

            # if the node's value is greater than the current node's value, go to the right subtree
            elif node.get_value() > self.get_value():
                if self.__right is None:
                    self.__add_right(node)
                    return True
                else:
                    return self.__right.add(node)

            # else if the node's value is equal to the current node's value, do nothing
            else:
                return False
        else:
            raise TypeError("The node can add only a node as its child.")

    def delete(self, value):
        """
        this method deletes a node with a certain value considering only child nodes
        :param value: the value of the node to delete
        :raises KeyError: if there is no node with the given value
        """

        if self.get_value() == value:
            # if we are deleting a node with no children, just delete the node
            if self.__left is None and self.__right is None:
                if self.__parent is not None:
                    if self.__parent.get_left() == self:
                        self.__parent.set_left(None)
                    elif self.__parent.get_right() == self:
                        self.__parent.set_right(None)

                # case when we are deleting the root of the tree with no children
                else:
                    self.__value = None

            # else if the node we are deleting has a left child, the left child takes the place of the node
            # we are deleting
            elif self.__right is None:
                if self.__parent is not None:
                    if self.__parent.get_left() == self:
                        self.__parent.set_left(self.__left)
                    elif self.__parent.get_right() == self:
                        self.__parent.set_right(self.__left)
                    self.__left.set_parent(self.__parent)

                # case when we are deleting the root of the tree with only a left child
                else:
                    self.__value = self.__left.get_value()
                    self.__right = self.__left.get_right()
                    self.__left = self.__left.get_left()
                    self.__parent = None

            # else if the node we are deleting has a right child, the right child takes the place of the node
            # we are deleting
            elif self.__left is None:
                if self.__parent is not None:
                    if self.__parent.get_left() == self:
                        self.__parent.set_left(self.__right)
                    elif self.__parent.get_right() == self:
                        self.__parent.set_right(self.__right)
                    self.__right.set_parent(self.__parent)

                # case when we are deleting the root of the tree with only a right child
                else:
                    self.__value = self.__right.get_value()
                    self.__left = self.__right.get_left()
                    self.__right = self.__right.get_right()
                    self.__parent = None

            # else if the node we are deleting has two children, find the successor of the node,
            # shift the values of the node and the successor, and then delete the successor node
            else:
                if self.__right is not None:
                    successor = self.__right
                    while successor.get_left() is not None:
                        successor = successor.get_left()
                    successor_value = successor.get_value()
                    self.delete(successor_value)
                    self.__value = successor_value

                # case when we are deleting the root of the tree with two children
                else:
                    successor = self
                    while successor.get_parent().get_right() == self:
                        successor = successor.get_parent()
                    successor = successor.get_parent()
                    successor_value = successor.get_value()
                    self.delete(successor_value)
                    self.__value = successor_value

        # else if the current node's value is less than the value we want to delete and there is a right child
        # call the delete method for the right child
        elif self.get_value() < value and self.__right is not None:
            self.__right.delete(value)

        # else if the current node's value is greater than the value we want to delete and there is a left child
        # call the delete method for the left child
        elif self.get_value() > value and self.__left is not None:
            self.__left.delete(value)

        # else the element doesn't exist in the tree, hence raise a KeyError
        else:
            raise KeyError("You are trying to delete an element which doesn't exist in the tree.")

    def contains(self, value):
        """
        this method searches for a node with the given as argument value
        :param value: the value to search for
        :return: True if a node with the given value is found and False otherwise
        """

        if self.get_value() == value:
            return True

        # else if the current node's value is less than the argument value and there is a right child,
        # search in the right subtree
        elif self.get_value() is not None and self.get_value() < value and self.__right is not None:
            return self.__right.contains(value)

        # else if the current node's value is greater than the argument value and there is a left child,
        # search in the left subtree
        elif self.get_value() is not None and self.get_value() > value and self.__left is not None:
            return self.__left.contains(value)

        # else the element could not be found, hence return false
        else:
            return False

    def __add_left(self, node):
        """
        'private' method, used to add a node object as left child, intended to be used only in the scope of this class
        :param node: the node object to add
        :raises TypeError: if the type of the argument is not Node
        """

        if type(node) == Node:
            self.__left = node
            self.__left.set_parent(self)
        else:
            raise TypeError("You can only add a Node as a left child.")

    def __add_right(self, node):
        """
        'private' method, used to add a node object as right child, intended to be used only in the scope of this class
        :param node: the node object to add
        :raises TypeError: if the type of the argument is not Node
        """

        if type(node) == Node:
            self.__right = node
            self.__right.set_parent(self)
        else:
            raise TypeError("You can only add a Node as a right child.")


class BinaryHeap(ABC):
    """
    implementation for the Abstract Data Structure called Binary Heap, the class extends the ABC class, which makes it
    an abstract class, which cannot be instantiated directly, instead one should use MinBinaryHeap and MaxBinaryHeap
    """

    def __init__(self, elements_type=int):
        """
        a constructor for the BinaryHeap class
        :param elements_type: optional argument, default value is int, only elements of this type can be added
            to the heap
        :raises TypeError: if the 'elements_type' argument is specified and is not a valid type
        """

        if type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        self.__elements = []  # the elements in the heap are stored in a python list
        self.__elements_type = elements_type

    def __len__(self):
        """
        overriding this method allows the use of the 'len(heap)' syntax
        :return: calls the size() method to get the number of elements in the heap
        """

        return self.size()

    def __str__(self):
        """
        this is the string representation of the heap
        :return: the string representation of the list of elements in the heap
        """

        return str(self.__elements)

    def __contains__(self, item):
        """
        overriding this method allows the use of the 'item in heap' syntax
        :param item: the item to search for in the heap
        :return: calls the contains() method to check if the given item is contained in the heap
        """

        return self.contains(item)

    @abstractmethod
    def __iter__(self):
        """
        defining this as an abstract method requires all child classes to give implementation for an iterator
        """

        pass

    @abstractmethod
    def __next__(self):
        """
        defining this as an abstract method requires all child classes to give implementation for the next method
        """

        pass

    def is_empty(self):
        """
        this method checks if the size of the heap is 0
        :return: True if there are no elements in the heap and False otherwise
        """

        return self.size() == 0

    def size(self):
        """
        this method gets the size of the heap
        :return: the number of elements in the heap
        """

        return len(self.__elements)

    def type(self):
        """
        this method gets the type of elements allowed to be added in the heap
        :return: the type of elements in the heap
        """

        return self.__elements_type

    def contains(self, item):
        """
        this method checks if an element is contained in the heap
        :param item: the item to search for
        :return: True if the heap contains this item and False otherwise
        """

        if type(item) == self.__elements_type:
            return item in self.__elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elements_type))

    def add(self, element):
        """
        this method adds an element in the heap
        :param element: the element to add
        :raises TypeError: if the argument's type is different from the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            self.__elements.append(element)

            self.__percolate_up()
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elements_type))

    @abstractmethod
    def __percolate_up(self):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def __percolate_down(self):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def get_sorted_elements(self):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def replace_root(self, element):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def replace(self, old_element, new_element):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def remove(self, element):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass


# noinspection PyAbstractClass,PyPep8Naming
class MinBinaryHeap(BinaryHeap):
    """
    Abstract Data Structure - represents a binary heap, with its minimum element being the root of the tree
    """

    def __init__(self, elements_type=int):
        """
        constructor for MinBinaryHeap,
        calls the parent class constructor and sets new references to the heap's elements list and type
        :param elements_type: the type of elements allowed in the heap
        :raises TypeError: if elements_type is not a valid type
        """

        if type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        if elements_type is None:
            elements_type = int
        BinaryHeap.__init__(self, elements_type)

        self.__elements = self._BinaryHeap__elements
        self.__elements_type = self._BinaryHeap__elements_type

    def __iter__(self):
        """
        overriding this method allows the use of an iterator for the binary heap
        :return: reference to the heap object itself
        """
        return self

    def __next__(self):
        """
        overriding this method so that the iterator knows which element to return
        :return: the min element in the heap and removes it
        :raises StopIteration: if the heap is empty
        """

        if not self.is_empty():
            return self.remove_min()
        else:
            raise StopIteration

    def _BinaryHeap__percolate_up(self):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to use after the add operation
        """

        # get the last element in the list
        child = len(self.__elements) - 1

        # find its correct place in the heap
        while child > 0:
            parent = int((child - 1)/2)
            if self.__elements[child] >= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp
            child = parent

    def _BinaryHeap__percolate_down(self):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to use after the a remove_min operation
        """

        # get the first element in the heap
        parent = 0
        child = 2*parent + 1

        # find its correct place in the heap
        while child < len(self.__elements):
            if child + 1 < len(self.__elements):
                if self.__elements[child] > self.__elements[child+1]:
                    child += 1

            if self.__elements[child] >= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp

            parent = child
            child = 2*parent + 1

    def peek_min(self):
        """
        this method gets the minimum element in the heap without removing it
        :return: minimum element or None if there are no elements in the heap
        """

        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    def remove_min(self):
        """
        this method removes the minimum element from the heap
        :return: the minimum element in the heap
        :raises ValueError: if there are no elements in the heap
        """

        if len(self.__elements) > 0:
            min_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()
            self._BinaryHeap__percolate_down()

            return min_element
        else:
            raise ValueError("There are no elements in the heap")

    def get_sorted_elements(self):
        """
        the difference between this method and the iterator is that after this function is finished the heap's
        elements are preserved
        :returns: a list with the sorted elements in the heap starting from the minimum entry
        """

        temp_elements = [k for k in self.__elements]
        sorted_elements = []

        while len(self.__elements) > 0:
            sorted_elements.append(self.remove_min())

        self.__elements = temp_elements
        # noinspection PyAttributeOutsideInit
        self._BinaryHeap__elements = temp_elements

        return sorted_elements

    def replace_root(self, element):
        """
        removes and returns the smallest element in the heap and adds the new element, this method will
        perform better than using remove_min() and add() for this purpose
        :param element: the new element to replace the root
        :return: the smallest element in the heap
        :raises ValueError: if there are no elements in the heap
        :raises TypeError: if the type of the argument is different than the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise ValueError("There are no elements in the heap")
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elements_type))

    def replace(self, old_element, new_element):
        """
        this method replaces an element in the heap with a new element and adjusts the order
        :param old_element: the element to replace
        :param new_element: the new element
        :raises TypeError: if the type of any of the arguments is not the same as the type of elements in the heap
        :raises KeyError: if the old element is not contained in the heap
        """

        if type(old_element) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if type(new_element) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        replaced = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == old_element:
                self.__elements[index] = new_element

                parent = index
                child = 2*parent + 1
                while child < len(self.__elements):
                    if child + 1 < len(self.__elements):
                        if self.__elements[child] > self.__elements[child + 1]:
                            child += 1

                    if self.__elements[child] >= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp

                    parent = child
                    child = 2 * parent + 1

                child = index
                while child > 0:
                    parent = int((child - 1) / 2)
                    if self.__elements[child] >= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp
                    child = parent

                replaced = True
                break

        if not replaced:
            raise KeyError("The element you are trying to replace is not contained in the heap.")

    def remove(self, element):
        """
        this method removes an element in the heap
        :param element: the element to remove
        :raises TypeError: if the type of the argument is not the same as the type of the elements in the heap
        :raises KeyError: if the element to remove is not contained in the heap
        """

        if type(element) != self.__elements_type:
            raise TypeError("The argument is not of type " + str(self.__elements_type))

        removed = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == element:
                self.__elements[index] = self.__elements[len(self.__elements) - 1]
                self.__elements.pop()

                parent = index
                child = 2 * parent + 1
                while child < len(self.__elements):
                    if child + 1 < len(self.__elements):
                        if self.__elements[child] > self.__elements[child + 1]:
                            child += 1

                    if self.__elements[child] >= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp

                    parent = child
                    child = 2 * parent + 1

                child = index
                if child < len(self.__elements):
                    while child > 0:
                        parent = int((child - 1) / 2)
                        if self.__elements[child] >= self.__elements[parent]:
                            break

                        temp = self.__elements[child]
                        self.__elements[child] = self.__elements[parent]
                        self.__elements[parent] = temp
                        child = parent

                removed = True
                break

        if not removed:
            raise KeyError("The element you are trying to remove is not contained in the heap.")


# noinspection PyAbstractClass,PyPep8Naming
class MaxBinaryHeap(BinaryHeap):
    """
    Abstract Data Structure - represents a binary heap, with its maximum element being the root of the tree
    """

    def __init__(self, elements_type=int):
        """
        constructor for MaxBinaryHeap,
        calls the parent class constructor and sets new references to the heap's elements list and type
        :param elements_type: the type of elements allowed in the heap
        :raises TypeError: if elements_type is not a valid type
        """

        if type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        if elements_type is None:
            elements_type = int
        BinaryHeap.__init__(self, elements_type)

        self.__elements = self._BinaryHeap__elements
        self.__elements_type = self._BinaryHeap__elements_type

    def __iter__(self):
        """
        overriding this method allows the use of an iterator for the binary heap
        :return: reference to the heap object itself
        """

        return iter(self.get_sorted_elements())

    def __next__(self):
        """
        overriding this method so that the iterator knows which element to return
        :return: the max element in the heap and removes it
        :raises StopIteration: if the heap is empty
        """

        if not self.is_empty():
            return self.remove_max()
        else:
            raise StopIteration

    def _BinaryHeap__percolate_up(self):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to use after the add operation
        """

        # get the last element in the heap
        child = len(self.__elements) - 1

        # find its place in the heap
        while child > 0:
            parent = int((child - 1)/2)
            if self.__elements[child] <= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp
            child = parent

    def _BinaryHeap__percolate_down(self):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to use after the a remove_max operation
        """

        # get the first element in the heap
        parent = 0
        child = 2*parent + 1

        # find its place in the heap
        while child < len(self.__elements):
            if child + 1 < len(self.__elements):
                if self.__elements[child] < self.__elements[child+1]:
                    child += 1

            if self.__elements[child] <= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp

            parent = child
            child = 2*parent + 1

    def peek_max(self):
        """
        this method gets the maximum element in the heap without removing it
        :return: maximum element or None if there are no elements in the heap
        """

        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    def remove_max(self):
        """
        this method removes the maximum element from the heap
        :return: the maximum element in the heap
        :raises ValueError: if there are no elements in the heap
        """

        if len(self.__elements) > 0:
            max_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()
            self._BinaryHeap__percolate_down()

            return max_element
        else:
            raise ValueError("There are no elements in the heap")

    def get_sorted_elements(self):
        """
        the difference between this method and the iterator is that after this function is finished the heap's
        elements are preserved
        :returns: a list with the sorted elements in the heap starting from the maximum entry
        """

        temp_elements = [k for k in self.__elements]
        sorted_elements = []

        while len(self.__elements) > 0:
            sorted_elements.append(self.remove_max())

        self.__elements = temp_elements
        # noinspection PyAttributeOutsideInit
        self._BinaryHeap__elements = temp_elements

        return sorted_elements

    def replace_root(self, element):
        """
        removes and returns the largest element in the heap and adds the new element, this method will
        perform better than using remove_max() and add() for this purpose
        :param element: the new element to replace the root
        :return: the largest element in the heap
        :raises ValueError: if there are no elements in the heap
        :raises TypeError: if the type of the argument is different than the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise ValueError("There are no elements in the heap")
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elements_type))

    def replace(self, old_element, new_element):
        """
        this method replaces an element in the heap with a new element and adjusts the order
        :param old_element: the element to replace
        :param new_element: the new element
        :raises TypeError: if the type of any of the arguments is not the same as the type of elements in the heap
        :raises KeyError: if the old element is not contained in the heap
        """

        if type(old_element) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if type(new_element) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        replaced = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == old_element:
                self.__elements[index] = new_element

                parent = index
                child = 2*parent + 1
                while child < len(self.__elements):
                    if child + 1 < len(self.__elements):
                        if self.__elements[child] < self.__elements[child + 1]:
                            child += 1

                    if self.__elements[child] <= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp

                    parent = child
                    child = 2 * parent + 1

                child = index
                while child > 0:
                    parent = int((child - 1) / 2)
                    if self.__elements[child] <= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp
                    child = parent

                replaced = True
                break

        if not replaced:
            raise KeyError("The element you are trying to replace is not contained in the heap.")

    def remove(self, element):
        """
        this method removes an element in the heap
        :param element: the element to remove
        :raises TypeError: if the type of the argument is not the same as the type of the elements in the heap
        :raises KeyError: if the element to remove is not contained in the heap
        """

        if type(element) != self.__elements_type:
            raise TypeError("The argument is not of type " + str(self.__elements_type))

        removed = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == element:
                self.__elements[index] = self.__elements[len(self.__elements) - 1]
                self.__elements.pop()

                parent = index
                child = 2 * parent + 1
                while child < len(self.__elements):
                    if child + 1 < len(self.__elements):
                        if self.__elements[child] < self.__elements[child + 1]:
                            child += 1

                    if self.__elements[child] <= self.__elements[parent]:
                        break

                    temp = self.__elements[child]
                    self.__elements[child] = self.__elements[parent]
                    self.__elements[parent] = temp

                    parent = child
                    child = 2 * parent + 1

                child = index
                if child < len(self.__elements):
                    while child > 0:
                        parent = int((child - 1) / 2)
                        if self.__elements[child] <= self.__elements[parent]:
                            break

                        temp = self.__elements[child]
                        self.__elements[child] = self.__elements[parent]
                        self.__elements[parent] = temp
                        child = parent

                removed = True
                break

        if not removed:
            raise KeyError("The element you are trying to remove is not contained in the heap.")


class PriorityQueue(object):
    """
    Abstract Data Structure - represents a queue with priorities for elements
    """

    def __init__(self, elements_type=None, reverse=False):
        """
        constructor for the priority queue
        :param elements_type: denotes the type of elements that can be added to the queue, defualt is None, which allows
            all types of elements
        :param reverse: a boolean, which represents what kind of priority queue to use - if set to False(default) then
            the dequeue() function returns the element with the greatest priority, if set to True - it returns the
            element with the least priority
        """

        if elements_type is not None and type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        if type(reverse) != bool:
            raise TypeError(str(reverse) + " is not a valid boolean variable")

        if not reverse:
            self.__indices = MaxBinaryHeap(int)
        else:
            self.__indices = MinBinaryHeap(int)

        self.__elements = {}
        self.__elements_type = elements_type

    def __str__(self):
        """
        a string representation of the priority queue
        :return: the str representation of the dictionary with elements in the queue
        """

        return str(self.__elements)

    def __len__(self):
        """
        overriding this method allows the 'len(priority_queue) syntax'
        :return: the number of elements in the queue
        """
        return self.size()

    def __contains__(self, priority):
        """
        overriding this method allows the 'element in priority_queue' syntax
        :param priority: the priority to search for
        :return: True if there is an element linked to this priority and False otherwise
        """

        return self.contains(priority)

    def __iter__(self):
        """
        overriding this method allows the use of an iterator with the priority queue
        :return: reference to the queue itself
        """

        return self

    def __next__(self):
        """
        the next method used for the iterator
        :return: uses dequeue to return the next element
        :raises StopIteration: if the queue is empty
        """

        if self.is_empty():
            raise StopIteration
        else:
            return self.dequeue()

    def is_empty(self):
        """
        this method checks if the size of the queue is 0
        :return: True if there are no elements in the queue and False otherwise
        """

        return self.size() == 0

    def size(self):
        """
        this method gets the size of the queue
        :return: the number of elements in the queue
        """

        return len(self.__elements)

    def type(self):
        """
        a getter for the type of elements in the queue
        :return: the type of elements allowed in the queue
        """

        return self.__elements_type

    def is_reversed(self):
        """
        this method checks if the queue is reversed
        :return: True if the dequeue function returns the element in the least priority and False otherwise
        """

        return type(self.__indices) == MinBinaryHeap

    def enqueue(self, item, priority):
        """
        this method inserts an element into the queue with a given priority,
        if the priority argument already exists in the queue, the element stored with this priority will be overwritten
        by the new element
        :param item: the item to insert
        :param priority: the priority of the item
        :raises TypeError: if the priority argument is not an integer
        :raises TypeError: if the element to enqueue is not of the same type as the other elements in the queue
            asserting that the type of the queue is not None (all types allowed in this case)
        """

        if type(priority) != int:
            raise TypeError("The priority must be an integer")

        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The element you are trying to enqueue is not of type " + str(self.__elements_type))

        if priority not in self.__elements:
            self.__indices.add(priority)
        self.__elements[priority] = item

    def dequeue(self):
        """
        this method takes the element with the greatest or the lowest priority depending on the reverse argument in the
        constructor, then returns it and removes it from the queue
        :return: the element to be dequeued
        :raises ValueError: if the queue is empty
        """

        if self.is_empty():
            raise ValueError("The priority queue doesn't contain any elements")

        if type(self.__indices) == MinBinaryHeap:
            min_priority = self.__indices.remove_min()
            element_to_return = self.__elements.get(min_priority)
            self.__elements.pop(min_priority)
            return element_to_return
        elif type(self.__indices) == MaxBinaryHeap:
            max_priority = self.__indices.remove_max()
            element_to_return = self.__elements.get(max_priority)
            self.__elements.pop(max_priority)
            return element_to_return

    def peek(self):
        """
        this method is the same as dequeue() but doesn't remove the element from the priority queue
        :return: the element to be dequeued without removing it or None if the queue is empty
        """

        if self.is_empty():
            return None

        if type(self.__indices) == MinBinaryHeap:
            return self.__elements.get(self.__indices.peek_min())
        elif type(self.__indices) == MaxBinaryHeap:
            return self.__elements.get(self.__indices.peek_max())

    def get(self, priority):
        """
        this method gets the element with a specified priority
        :param priority: the given priority
        :return: the element linked to this priority or None if not existing
        :raises TypeError: if the priority is not of type int
        """

        if type(priority) != int:
            raise TypeError("The priority parameter must be an integer.")

        return self.__elements.get(priority)

    def contains(self, priority):
        """
        this method checks if a given priority is assigned to an object
        :param priority: the priority to check
        :return: True if the queue contains this priority and False otherwise
        :raises TypeError: if the priority is not of type int
        """

        if type(priority) == int:
            return priority in self.__elements.keys()
        else:
            raise TypeError("Priorities must be of type int")

    def contains_element(self, element):
        """
        this method checks if a given element is contained in the queue
        :param element: the element to check
        :return: True if the element is in the queue and False otherwise
        :raises TypeError: if the element's type is not the same as the type of elements in the queue
        """

        if self.__elements_type is not None and type(element) != self.__elements_type:
            raise TypeError("Type of the parameter is not " + str(self.__elements_type))

        return element in self.__elements.values()

    def replace_priority(self, element, new_priority, comparison=None):
        """
        this method finds an element and replaces its priority with a new one
        :param element: the element, for which the priority must be replaced
        :param new_priority: the new priority
        :param comparison: represents whether a comparison between the two priorities must be made before replacing
            None - no comparison, 1 - greater than comparison (new > old)), -1 - less than comparison (new < old)
        :return: True if the element's priority has been replaced and False otherwise
        :raises TypeError: if the type of the queue is not None and is different than the type of the element argument
        :raises TypeError: if the type of the new priority is not int
        :raises ValueError if the type of the comparison argument is not any of these (None, -1, 1)
        :raises KeyError: if the element is not contained in the queue
        """

        if self.__elements_type is not None and type(element) != self.__elements_type:
            raise TypeError("Type of the first parameter is not " + str(self.__elements_type))

        if type(new_priority) != int:
            raise TypeError("The priority parameter must be an integer.")

        if comparison is not None and comparison != 1 and comparison != -1:
            raise ValueError("The comparison argument must be None for no comparison, -1 - for less than comparison"
                             "and 1 for greater than comparison")

        element_found = False
        replaced = False
        for priority in self.__elements:
            if self.__elements[priority] == element:
                if (comparison is None and priority != new_priority) or (comparison == 1 and new_priority > priority)\
                            or (comparison == -1 and new_priority < priority):
                    self.__elements.pop(priority)
                    if new_priority not in self.__indices:
                        self.__indices.replace(priority, new_priority)
                    else:
                        self.__indices.remove(priority)
                    self.__elements[new_priority] = element
                    replaced = True
                element_found = True
                break

        if not element_found:
            raise KeyError("The queue doesn't contain the element for which you are trying to replace the priority.")

        return replaced

    def remove_element(self, element):
        """
        this method removes an element from the priority queue
        :param element: the element to remove
        :raises KeyError: if the queue doesn't contain the element to delete
        """

        if self.__elements_type is not None and type(element) != self.__elements_type:
            raise TypeError("Type of the parameter is not " + str(self.__elements_type))

        removed = False
        for priority in self.__elements:
            test_element = self.__elements[priority]
            if element == test_element:
                self.__indices.remove(priority)
                self.__elements.pop(priority)
                removed = True
                break

        if not removed:
            raise KeyError("The queue doesn't contain the element you are trying to delete.")


class DuplicatePriorityQueue(PriorityQueue):
    """
    Abstract Data Structure - represents a queue with priorities for elements, difference from PriorityQueue is that
    this implementation allows elements with duplicated priorities
    """

    def __init__(self, elements_type=None, reverse=False):
        """
        overriding the constructor to get references to the elements and the priorities
        :param elements_type: the type of elements in the queue
        :param reverse: the reverse argument of the PriorityQueue
        """

        super().__init__(elements_type, reverse)
        self.__elements = self._PriorityQueue__elements
        self.__indices = self._PriorityQueue__indices
        self.__size = 0

    def size(self):
        """
        overriding the size() method to return the __size attribute
        :return: the number of elements in the queue (including duplicated priorities)
        """

        return self.__size

    def enqueue(self, item, priority):
        """
        overriding the enqueue() method to allow dupicated priorities,
        2 or more elements with the same priorities are stored in a queue
        :param item: the item to enqueue
        :param priority: the priority of the item
        :raises TypeError: if the type of the priority is not int
        :raises TypeError: if the element to enqueue is not of the same type as the other queue's elements
        """

        if type(priority) != int:
            raise TypeError("The priority must be an integer")

        if self.type() is not None and type(item) != self.type():
            raise TypeError("The element you are trying to enqueue is not of type " + str(self.type()))

        if priority not in self.__elements:
            self.__indices.add(priority)
            self.__elements[priority] = item
        else:
            element = self.__elements[priority]
            if type(element) == Queue:
                element.enqueue(item)
            else:
                duplicates = Queue(self.type())
                duplicates.enqueue(element)
                duplicates.enqueue(item)
                self.__elements[priority] = duplicates
        self.__size += 1

    def dequeue(self):
        """
        overriding the dequeue() method to handle duplicated priorities too
        :return: the dequeued element
        :raises ValueError: if the queue is empty
        """
        if self.is_empty():
            raise ValueError("The priority queue doesn't contain any elements")

        if type(self.__indices) == MinBinaryHeap:
            min_priority = self.__indices.peek_min()
            element_to_return = self.__elements.get(min_priority)
            if type(element_to_return) != Queue:
                self.__indices.remove_min()
                self.__elements.pop(min_priority)
                self.__size -= 1
                return element_to_return
            else:
                if len(element_to_return) == 2:
                    to_return = element_to_return.dequeue()
                    self.__elements[min_priority] = element_to_return.dequeue()
                    self.__size -= 1
                    return to_return
                else:
                    self.__size -= 1
                    return element_to_return.dequeue()

        elif type(self.__indices) == MaxBinaryHeap:
            max_priority = self.__indices.peek_max()
            element_to_return = self.__elements.get(max_priority)
            if type(element_to_return) != Queue:
                self.__indices.remove_max()
                self.__elements.pop(max_priority)
                self.__size -= 1
                return element_to_return
            else:
                if len(element_to_return) == 2:
                    to_return = element_to_return.dequeue()
                    self.__elements[max_priority] = element_to_return.dequeue()
                    self.__size -= 1
                    return to_return
                else:
                    self.__size -= 1
                    return element_to_return.dequeue()

    def peek(self):
        """
        overriding the peek method to handle duplicated priorities too
        :return: the element to be dequeued but doesn't remove it or None if the queue is empty
        """

        if self.is_empty():
            return None

        to_peek = None
        if type(self.__indices) == MinBinaryHeap:
            to_peek = self.__elements.get(self.__indices.peek_min())
        elif type(self.__indices) == MaxBinaryHeap:
            to_peek = self.__elements.get(self.__indices.peek_max())

        if type(to_peek) != Queue:
            return to_peek
        else:
            return to_peek.peek()

    def get(self, priority):
        """
        overriding the get method to handle duplicated priorities
        :param priority: the priority to search for
        :return: the element linked to the given priority
        :raises TypeError: if the priority's type is not int
        """

        if type(priority) != int:
            raise TypeError("The priority parameter must be an integer.")
        element = self.__elements.get(priority)
        if type(element) != Queue:
            return element
        else:
            return element.peek()

    def contains_element(self, element):
        """
        overriding the contains_element method to search for values with duplicated priorities too
        :param element: the element to search for
        :return: True if the element is contained in the queue and False otherwise
        :raises TypeError: if the element's type is not the same as the type of queue's elements
        """

        if self.type() is not None and type(element) != self.type():
            raise TypeError("Type of the parameter is not " + str(self.type()))

        if not self.has_duplicates():
            return super().contains_element(element)

        for test_element in self.__elements.values():
            if type(test_element) != Queue and test_element == element:
                return True
            elif type(test_element) == Queue:
                if element in test_element:
                    return True
        return False
    
    def has_duplicates(self):
        """
        a method for fast check if there are items with duplicated priorities
        :return: True if there are two or more elements with the same priority and False otherwise
        """

        return self.size() != len(self.__elements)

    def replace_priority(self, element, new_priority, comparison=None):
        """
        overriding the replace_priority method to work with duplicated priorities too
        :param element: the element, for which the priority must be replaced
        :param new_priority: the new priority
        :param comparison: represents whether a comparison between the two priorities must be made before replacing
            None - no comparison, 1 - greater than comparison (new > old)), -1 - less than comparison (new < old)
        :return: True if the element's priority has been replaced and False otherwise
        :raises TypeError: if the type of the queue is not None and is different than the type of the element argument
        :raises TypeError: if the type of the new priority is not int
        :raises ValueError if the type of the comparison argument is not any of these (None, -1, 1)
        :raises KeyError: if the element is not contained in the queue
        :return:
        """

        if self.type() is not None and type(element) != self.type():
            raise TypeError("Type of the first parameter is not " + str(self.type()))

        if type(new_priority) != int:
            raise TypeError("The priority parameter must be an integer.")

        if comparison is not None and comparison != 1 and comparison != -1:
            raise ValueError("The comparison argument must be None for no comparison, -1 - for less than comparison"
                             "and 1 for greater than comparison")

        element_found = False
        replaced = False
        for priority in self.__elements:
            test_element = self.__elements[priority]
            if type(test_element) == Queue:
                if element in test_element:
                    if (comparison is None and priority != new_priority) or \
                            (comparison == 1 and new_priority > priority)\
                            or (comparison == -1 and new_priority < priority):
                        test_element.remove(element)
                        if len(test_element) == 1:
                            self.__elements[priority] = test_element.dequeue()

                        if new_priority not in self.__indices:
                            self.__indices.add(new_priority)
                            self.__elements[new_priority] = element
                        else:
                            if type(self.__elements[new_priority]) == Queue:
                                self.__elements[new_priority].enqueue(element)
                            else:
                                duplicates = Queue(self.type())
                                duplicates.enqueue(self.__elements[new_priority])
                                duplicates.enqueue(element)
                                self.__elements[new_priority] = duplicates

                        replaced = True
                    element_found = True
                    break
            else:
                if test_element == element:
                    if (comparison is None and priority != new_priority) or \
                            (comparison == 1 and new_priority > priority) \
                            or (comparison == -1 and new_priority < priority):
                        self.__elements.pop(priority)
                        if new_priority not in self.__indices:
                            self.__indices.replace(priority, new_priority)
                            self.__elements[new_priority] = element
                        else:
                            self.__indices.remove(priority)
                            if type(self.__elements[new_priority]) == Queue:
                                self.__elements[new_priority].enqueue(element)
                            else:
                                duplicates = Queue(self.type())
                                duplicates.enqueue(self.__elements[new_priority])
                                duplicates.enqueue(element)
                                self.__elements[new_priority] = duplicates
                        replaced = True
                    element_found = True
                    break

        if not element_found:
            raise KeyError("The queue doesn't contain the element for which you are trying to replace the priority.")

        return replaced

    def remove_element(self, element):
        """
        overriding the remove() method to handle duplicated priorities too
        :param element: the element to remove
        :raises TypeError: if the type of the argument is not the same as the type of the elements in the heap
        :raises KeyError: if the element to remove is not contained in the heap
        """

        if self.type() is not None and type(element) != self.type():
            raise TypeError("Type of the parameter is not " + str(self.type()))

        removed = False
        for priority in self.__elements:
            test_element = self.__elements[priority]
            if type(test_element) == Queue:
                try:
                    test_element.remove(element)
                    if len(test_element) == 0:
                        self.__elements.pop(priority)
                        self.__indices.remove(priority)
                    elif len(test_element) == 1:
                        self.__elements[priority] = test_element.dequeue()
                    self.__size -= 1
                    removed = True
                    break
                except KeyError:
                    pass
            else:
                if element == test_element:
                    self.__indices.remove(priority)
                    self.__elements.pop(priority)
                    self.__size -= 1
                    removed = True
                    break

        if not removed:
            raise KeyError("The queue doesn't contain the element you are trying to delete.")


# Abstract Data Type Graph
class Graph(object):

    # a constructor for the graph
    def __init__(self, elements_type=None, directed=False, oriented=False, weighted=False):
        if elements_type is not None and type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        self.__elements_type = elements_type

        if oriented and not directed:
            raise ValueError("A graph cannot be oriented and not directed at the same time")

        self.__directed = directed
        self.__oriented = oriented
        self.__weighted = weighted
        self.__nodes_set = set()
        self.__nodes_list = []
        self.__edges = []
        for i in range(5):
            none_list = []
            for j in range(5):
                none_list.append(None)
            self.__edges.append(none_list)

    # len(graph) method
    def __len__(self):
        return self.size()

    # string representation for the graph
    def __str__(self):
        return "Graph: directed - " + str(self.__directed) + ", oriented - " + str(self.__oriented) + \
               ", weighted - " + str(self.__weighted)

    # iterator for the graph
    def __iter__(self):
        return iter(self.__nodes_list)

    # the 'element in graph' method
    def __contains__(self, item):
        return self.contains(item)

    # returns the number of nodes in the graph
    def size(self):
        return len(self.__nodes_set)

    # is_empty method checks if the size of the graph is 0
    def is_empty(self):
        return self.size() == 0

    # a method to return the type of elements in the graph
    def type(self):
        return self.__elements_type

    # a method to return whether the graph is weighted
    def is_weighted(self):
        return self.__weighted

    # a method to return whether the graph is oriented
    def is_oriented(self):
        return self.__oriented

    # a method to return whether the graph is directed
    def is_directed(self):
        return self.__directed

    # returns whether the graph contains the element
    def contains(self, item):
        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The item you are trying to find is not of type " + str(self.__elements_type))

        return item in self.__nodes_set

    # checks if an edge from first_item to the second_item exists, returns the weight of the edge
    def contains_edge(self, first_item, second_item):
        if self.__elements_type is not None and type(first_item) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if self.__elements_type is not None and type(second_item) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        if first_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the first argument")

        if second_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the second argument")

        return self.__edges[self.__nodes_list.index(first_item)][self.__nodes_list.index(second_item)] is not None

    # get the weight of an edge of a weighted graph
    def get_edge_weight(self, first_item, second_item):
        if self.__elements_type is not None and type(first_item) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if self.__elements_type is not None and type(second_item) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        if first_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the first argument")

        if second_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the second argument")

        if not self.__weighted:
            raise ValueError("The graph is not weighted. Use the contains_edge method.")

        index_1 = self.__nodes_list.index(first_item)
        index_2 = self.__nodes_list.index(second_item)

        if self.__edges[index_1][index_2] is None:
            raise ValueError("The edge doesn't exist.")
        else:
            return self.__edges[index_1][index_2]

    # a getter method for the vertices of the graph, returns a copy of the list, so that the original list containing
    # the nodes of the graph is not manually altered by the user
    def nodes(self):
        return deepcopy(self.__nodes_list)

    # a getter method for the edges of the graph, returns a copy of the list, so that the original list containing
    # the edges of the graph is not manually altered by the user
    def edges(self):
        return deepcopy(self.__edges)

    # returns the connected nodes to the given item
    def edges_of(self, item):
        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The argument is not of type " + str(self.__elements_type))

        if item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the argument")

        init_index = self.__nodes_list.index(item)
        connected_nodes = []
        for index in range(len(self.__edges[init_index])):
            if self.__edges[init_index][index] is not None:
                connected_nodes.append(self.__nodes_list[index])

        return connected_nodes

    # the add method which adds a node to the graph
    def add_node(self, item):
        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The item you are trying to add is not of type " + str(self.__elements_type))

        if item is None:
            raise AttributeError("You cannot add None nodes to the graph")

        if item not in self.__nodes_set:
            self.__nodes_set.add(item)
            self.__nodes_list.append(item)

            if len(self.__nodes_set) > len(self.__edges):
                new_edges = []
                for i in range(2*len(self.__edges)):
                    node_edges = []
                    for j in range(2*len(self.__edges)):
                        try:
                            node_edges.append(self.__edges[i][j])
                        except IndexError:
                            node_edges.append(None)
                    new_edges.append(node_edges)

                self.__edges = new_edges

    # the remove method which removes a node from the graph
    def remove_node(self, item):
        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The item you are trying to remove is not of type " + str(self.__elements_type))

        if item in self.__nodes_set:
            index = self.__nodes_list.index(item)
            self.__nodes_set.remove(item)
            del self.__nodes_list[index]

            self.__edges[index] = []
            for i in range(len(self.__edges)):
                self.__edges[index].append(None)

            for node_edges in self.__edges:
                if node_edges[index] is not None:
                    node_edges[index] = None
        else:
            raise KeyError("The graph doesn't contain the node you are trying to delete")

    # the add_edge method which adds an edge between the two nodes
    def add_edge(self, first_item, second_item, edge_weight=None):
        if self.__elements_type is not None and type(first_item) != self.__elements_type:
            raise TypeError("The item from which you are trying to add an edge is not of type "
                            + str(self.__elements_type))

        if self.__elements_type is not None and type(second_item) != self.__elements_type:
            raise TypeError("The item to which you are trying to add an edge is not of type "
                            + str(self.__elements_type))

        if edge_weight is not None and (type(edge_weight) != float and type(edge_weight) != int):
            raise TypeError("The edge weight must be of type integer or float")

        if first_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the node from which you are trying to add an edge")

        if second_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the node to which you are trying to add an edge")

        first_index = self.__nodes_list.index(first_item)
        second_index = self.__nodes_list.index(second_item)

        weight = None
        if self.__weighted:
            if edge_weight is not None:
                weight = edge_weight
            else:
                raise ValueError("Edge weight cannot be none when the graph is weighted.")

        if self.__directed:
            if self.__oriented:
                if self.__edges[second_index][first_index] is None:
                    if self.__weighted:
                        self.__edges[first_index][second_index] = weight
                    else:
                        self.__edges[first_index][second_index] = 1
                else:
                    raise KeyError("The graph is oriented and an edge with this nodes already exists")
            else:
                if self.__weighted:
                    self.__edges[first_index][second_index] = weight
                else:
                    self.__edges[first_index][second_index] = 1
        else:
            if self.__weighted:
                self.__edges[first_index][second_index] = weight
                self.__edges[second_index][first_index] = weight
            else:
                self.__edges[first_index][second_index] = 1
                self.__edges[second_index][first_index] = 1

    # the remove_edge method which removes an edge between the two nodes
    def remove_edge(self, first_item, second_item):
        if self.__elements_type is not None and type(first_item) != self.__elements_type:
            raise TypeError("The item from which you are trying to remove an edge is not of type "
                            + str(self.__elements_type))

        if self.__elements_type is not None and type(second_item) != self.__elements_type:
            raise TypeError("The item to which you are trying to remove an edge is not of type "
                            + str(self.__elements_type))

        if first_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the node from which you are trying to remove an edge")

        if second_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the node to which you are trying to remove an edge")

        first_index = self.__nodes_list.index(first_item)
        second_index = self.__nodes_list.index(second_item)

        if self.__edges[first_index][second_index] is None:
            raise KeyError("The graph doesn't contain the edge you are trying to delete.")

        if self.__directed:
            self.__edges[first_index][second_index] = None
        else:
            self.__edges[first_index][second_index] = None
            self.__edges[second_index][first_index] = None

    # a method, which replaces an old node with the new_node by not removing the old node's edges
    def replace_node(self, old_node, new_node):
        if self.__elements_type is not None and type(old_node) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if self.__elements_type is not None and type(new_node) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        if old_node not in self.__nodes_set:
            raise KeyError("You cannot replace a node, which the graph doesn't contain.")

        if new_node in self.__nodes_set:
            raise KeyError("The new node is a node, which the graph already contains.")

        self.__nodes_set.remove(old_node)
        self.__nodes_set.add(new_node)
        self.__nodes_list[self.__nodes_list.index(old_node)] = new_node
