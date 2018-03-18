from ADTs.BinarySearchTreeErrors import *


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
        :raises BinarySearchTreeTypeError: if the 'elements_type' argument is not a valid type (int, str, float, etc.)
        :raises BinarySearchTreeTypeError: if a root is specified and its type is different from the type of the binary search tree
        """

        # variables used for the iterator of the binary tree
        self.__iterator_counter = None
        self.__current_item = None

        # check for a valid type
        if type(elements_type) != type:
            raise BinarySearchTreeTypeError("{0} is not a valid type.".format(elements_type))

        # initialising the binary search tree
        self.__elements_type = elements_type

        if root is None:
            self.__root = root
            self.__number_of_items = 0
        elif type(root) == elements_type:
            self.__root = Node(root)
            self.__number_of_items = 1
        else:
            raise BinarySearchTreeTypeError("The binary search tree can contain only elements of type {0}".format(elements_type))

    def __str__(self):
        """
        the string representation of the binary search tree

        :return: a string, which contains information about the tree, such as the root value
        """

        if self.__root is not None:
            return "Binary search tree with root: {0}".format(self.__root.get_value())
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

    def __iter__(self):
        """
        overriding this method allows the implementation of an iterator for the tree

        :return: a reference to the tree itself
        """

        # setting the instance variables used for the iteration
        self.__current_item = None
        self.__iterator_counter = 0

        return self

    def __next__(self):
        """
        overriding this method to implement the next() method for the iterator

        :return: the next item to iterate
        :raises StopIteration: if the iteration is over
        """

        if self.__iterator_counter is None or self.__iterator_counter == self.get_number_of_elements():
            self.__iterator_counter = None
            raise StopIteration

        else:
            if self.__iterator_counter == 0:
                self.__current_item = self.__get_minimum_node()
            else:
                # if the current item has a right child, go right and then go left as much as possible
                if self.__current_item.get_right() is not None:
                    successor = self.__current_item.get_right()
                    while successor.get_left() is not None:
                        successor = successor.get_left()

                    self.__current_item = successor

                # else if there is no right child, go up left as much as possible and then go right
                else:
                    successor = self.__current_item
                    while successor.get_parent() is not None and successor.get_parent().get_right() == successor:
                        successor = successor.get_parent()

                    if successor.get_parent() is None:
                        self.__iterator_counter = 0
                        raise StopIteration
                    else:
                        successor = successor.get_parent()

                    self.__current_item = successor

            self.__iterator_counter += 1
            return self.__current_item.get_value()

    def add(self, value):
        """
        this method adds a new element to the tree

        :param value: the value of the new node to add
        :raises BinarySearchTreeTypeError: if the type of the argument is different than the type of elements in the binary search tree
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
            raise BinarySearchTreeTypeError("The binary tree can contain only elements of type {0}".format(self.__elements_type))

    def contains(self, value):
        """
        this method checks if an element with a certain value exists in the tree

        :param value: the value to search for in the tree
        :return: True if the tree contains an element with this value and False otherwise
        :raises BinarySearchTreeTypeError: if the type of the argument is different than the type of elements in the binary search tree
        """

        if type(value) == self.__elements_type:
            return self.__root.contains(value)
        else:
            raise BinarySearchTreeTypeError("The binary tree can contain only elements of type {0}".format(self.__elements_type))

    def delete(self, value):
        """
        this method deletes an element with a certain value from the tree

        :param value: the value to delete
        :raises BinarySearchTreeTypeError: if the type of the argument is different than the type of elements in the binary search tree
        :raises BinarySearchTreeElementError: if there is no node with the given value in the tree
        """

        if self.is_empty():
            raise EmptyBinarySearchTreeError("You cannot delete an element from an empty binary search tree.")

        if type(value) == self.__elements_type:
            if self.__root.delete(value):
                self.__number_of_items -= 1
            else:
                raise BinarySearchTreeElementError("You are trying to delete an element which doesn't exist in the tree.")
        else:
            raise BinarySearchTreeTypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

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

    def is_empty(self):
        """
        this method checks if the tree has no elements

        :return: True if the number of elements in the tree is 0 and False otherwise
        """

        return self.get_number_of_elements() == 0

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

        min_node = self.__get_minimum_node()
        return min_node.get_value() if min_node is not None else None

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

        max_node = self.__get_maximum_node()
        return max_node.get_value() if max_node is not None else None

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
    a utility class, which represents a Node in the binary search tree (used for internal purposes - not to be manipulated outside the binary search tree class)
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
        """

        self.__left = node

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
        """

        self.__right = node

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
        """

        self.__parent = node

    def add(self, node):
        """
        this method adds a node to the current node as a child by determining the right place of the node

        :param node: the node to add
        :return: True if the element has been added and False otherwise
        """

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

    def delete(self, value):
        """
        this method deletes a node with a certain value considering only child nodes

        :param value: the value of the node to delete
        :return: True if the element has been deleted and False otherwise
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

            return True

        # else if the current node's value is less than the value we want to delete and there is a right child
        # call the delete method for the right child
        elif self.get_value() < value and self.__right is not None:
            return self.__right.delete(value)

        # else if the current node's value is greater than the value we want to delete and there is a left child
        # call the delete method for the left child
        elif self.get_value() > value and self.__left is not None:
            return self.__left.delete(value)

        # else the element doesn't exist in the tree, hence return False
        else:
            return False

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
        """

        self.__left = node
        self.__left.set_parent(self)

    def __add_right(self, node):
        """
        'private' method, used to add a node object as right child, intended to be used only in the scope of this class

        :param node: the node object to add
        """

        self.__right = node
        self.__right.set_parent(self)
