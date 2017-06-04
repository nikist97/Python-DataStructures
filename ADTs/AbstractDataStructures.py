# Abstract Data Type stack, Last In First Out (LIFO)
class Stack(object):

    # constructor for stack, optional argument elements_type (it's set to None if not provided)
    # if elements_type is None, the stack can contain elements of many types simultaneously
    # otherwise, it can contain only elements from the type specified in the constructor
    def __init__(self, elements_type=None):
        self.__elements = []
        self.__elementsType = elements_type

    # the string representation for the stack returns the elements of the stack
    def __str__(self):
        return str(self.__elements)

    # the len(stack) method
    def __len__(self):
        return self.size()

    # the is_empty method, which checks if the size of the stack is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the stack
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the stack elements
    def type(self):
        return self.__elementsType

    # the push method, which pushes an item into the stack
    def push(self, item):
        if self.__elementsType is None:
            self.__elements.append(item)

        # if the elementsType attribute is different than None,
        # check if the type of the new item is the required one; if it's not raise a TypeError
        else:
            if type(item) == self.__elementsType:
                self.__elements.append(item)
            else:
                raise TypeError("The element you are trying to push is not of type " + self.__elementsType)

    # the pop method, which takes out the last element that got in the stack;
    # it raises a ValueError if there is no element to pop (if size of the stack is 0)
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            raise ValueError("There are no elements in the stack")

    # the peek method, which returns the last element that got in the stack, but doesn't remove it from the stack;
    # it returns None if there is no element to peek at
    def peek(self):
        if len(self.__elements) > 0:
            return self.__elements[len(self.__elements) - 1]
        else:
            return None


# Abstract Data Type Queue, First In First Out (FIFO)
class Queue(object):

    # constructor for queue, optional argument elements_type (it's set to None if not provided)
    # if elements_type is None, the queue can contain elements of many types simultaneously
    # otherwise, it can contain only elements from the type specified in the constructor
    def __init__(self, elements_type=None):
        self.__elements = []
        self.__elementsType = elements_type

    # the string representation for the queue returns the elements of the queue
    def __str__(self):
        return str(self.__elements)

    # the len(queue) method
    def __len__(self):
        return self.size()

    # the is_empty method, which checks if the size of the queue is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the queue
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the queue elements
    def type(self):
        return self.__elementsType

    # the enqueue method, which inserts an item into the queue
    def enqueue(self, item):
        if self.__elementsType is None:
            self.__elements.append(item)

        # if the elementsType attribute is different than None,
        # check if the type of the new item is the required one; if it's not raise a TypeError
        else:
            if type(item) == self.__elementsType:
                self.__elements.append(item)
            else:
                raise TypeError("The element you are trying to push is not of type " + self.__elementsType)

    # the dequeue method, which removes the item that got first in the queue
    # it raises a ValueError if there is no element to dequeue(if size of the queue is 0)
    def dequeue(self):
        if len(self.__elements) > 0:
            element = self.__elements[0]
            new_elements = [self.__elements[x] for x in range(1, len(self.__elements))]
            self.__elements = new_elements
            return element
        else:
            raise ValueError("There are no elements in the queue")

    # the peek method, which returns the first element that got in the queue, but doesn't remove it from the queue;
    # it returns None if there is no element to peek at
    def peek(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None


# Abstract Data Type Binary Tree
class BinarySearchTree(object):

    # the constructor for the binary tree, it has a root as an optional argument, if the root is specified the tree
    # is initialised with a root, else it is initialized with no root, the elements of the tree must be from the type
    # specified in the constructor, the default type that is used is int
    def __init__(self, root=None, elements_type=int):
        # variables used when using the iterator of the binary tree
        self.__successor = None
        self.__iterator_limit = None
        self.__iterator_finished = None
        self.__current_item = None

        # initialising the type of the elements in the tree
        self.__elements_type = elements_type

        # if the value of the root is not specified, create a tree with None root and no elements
        if root is None:
            self.__root = root
            self.__number_of_items = 0
        # else if the value of the root is specified create a tree with a root : Node with the value of the argument
        elif root is not None and type(root) == elements_type:
            self.__root = Node(root)
            self.__number_of_items = 1
        # if the type of the root is not from the specified type, raise a TypeError
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(elements_type) + ".")

    # overriding the __contains__ method
    def __contains__(self, item):
        # calling the contains method of the binary tree
        return self.contains(item)

    # overriding the __len__ method
    def __len__(self):
        # calling the get_number_of_elements method of the binary tree
        return self.get_number_of_elements()

    # overriding the __iter__ method, so that we can go through the elements of the tree
    def __iter__(self):
        self.__current_item = self.__get_minimum_node()
        self.__successor = self.__current_item
        self.__iterator_limit = self.__get_maximum_node()
        self.__iterator_finished = False
        return self

    # overriding the __next__ method, so that we can use the iterator of the binary tree
    def __next__(self):
        # if the iteration is over, raise StopIteration
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

    # the add method, which adds a Node with the value given as an argument to the binary tree
    def add(self, value):
        # check for the type of the value
        if type(value) == self.__elements_type:
            # if root is empty, add the element to the root
            if self.__root is None or self.__root.get_value() is None:
                self.__root = Node(value)
                self.__number_of_items = 1

            # else call the Node add method
            else:
                if self.__root.add(Node(value)):
                    self.__number_of_items += 1

        # if the type of the argument is not int, raise a TypeError
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    # the contains method, which finds if an element exists in the binary tree
    def contains(self, value):
        # check if the argument's type is the specified elements' type
        if type(value) == self.__elements_type:
            # call the Node contains method
            return self.__root.contains(value)

        # if the type of the argument is not from the specified type, raise a TypeError
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    # the delete method, which deletes an element from the tree
    def delete(self, value):
        # check if the argument's type is specified elements' type
        if type(value) == self.__elements_type:
            # calling the Node delete method
            self.__root.delete(value)
            self.__number_of_items -= 1

        # if the type of the argument is not from the specified type, raise a TypeError
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    # a getter method for the root of the tree
    def get_root(self):
        if self.__root is None:
            return None
        else:
            return self.__root.get_value()

    # a getter method for the number of elements in the tree
    def get_number_of_elements(self):
        return self.__number_of_items

    # a getter method for the type of the elements in the binary search tree
    def type(self):
        return self.__elements_type

    # a getter method for the minimum element in the tree
    def get_minimum(self):
        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node.get_value()

    # a getter method for the minimum element in the tree, this one returns the Node element rather than just the value
    def __get_minimum_node(self):
        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node

    # a getter method for the maximum element in the tree
    def get_maximum(self):
        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node.get_value()

    # a getter method for the maximum element in the tree, this one returns the Node element rather than just the value
    def __get_maximum_node(self):
        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node


# the Node class, which represents a Node for the binary Tree
class Node(object):

    # the constructor for the Node class
    def __init__(self, value):
        # a node has a value, a left and right child, a parent
        self.__value = value
        self.__left = None
        self.__right = None
        self.__parent = None

    # a getter method for the value of the Node
    def get_value(self):
        return self.__value

    # a getter method for the left child
    def get_left(self):
        return self.__left

    # a setter method for the left child
    def set_left(self, node=None):
        # check if the argument's type is Node or None
        if node is None or type(node) == Node:
            self.__left = node

        # if the argument's type is not Node or None, raise a TypeError
        else:
            raise TypeError("The child of a node must be a node.")

    # a getter method for the right child
    def get_right(self):
        return self.__right

    # a setter method for the right child
    def set_right(self, node=None):
        # check if the argument's type is Node or None
        if node is None or type(node) == Node:
            self.__right = node

        # if the argument's type is not Node or None, raise a TypeError
        else:
            raise TypeError("The child of a node must be a node.")

    # a getter method for the parent of the node
    def get_parent(self):
        return self.__parent

    # a setter method for the parent of the node
    def set_parent(self, node=None):
        # check if the argument's type is Node or None
        if node is None or type(node) == Node:
            self.__parent = node

        # if the argument's type is not Node or None, raise a TypeError
        else:
            raise TypeError("The parent of a node must be a node.")

    # the add method, which adds a node to the current node as a child,
    # the method returns a boolean representing whether the tree has added an element or not
    def add(self, node):
        # check if the argument's type is Node
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

        # if the argument's type is not Node, raise a TypeError
        else:
            raise TypeError("The node can add only a node as its child.")

    # the delete method of the Node class, which deletes a node
    def delete(self, value):
        # if the current node's value is the value we want to delete, proceed with the delete method
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

    # the contains method, which searches for the value given as an argument
    def contains(self, value):
        # if the current node's value is equal to the argument value, the element is found, hence return true
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

    # the add_left method, which adds a left child to the node and adjust the parent of the node argument
    def __add_left(self, node):
        # check if the argument's type is Node
        if type(node) == Node:
            self.__left = node
            self.__left.set_parent(self)

        # if the argument's type is not Node, raise a TypeError
        else:
            raise TypeError("You can only add a Node as a left child.")

    def __add_right(self, node):
        # check if the argument's type is Node
        if type(node) == Node:
            self.__right = node
            self.__right.set_parent(self)

        # if the argument's type is not Node, raise a TypeError
        else:
            raise TypeError("You can only add a Node as a right child.")
