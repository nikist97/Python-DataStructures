from DataStructures.BinarySearchTreeErrors import *
from DataStructures.BinaryHeapErrors import *
from abc import ABC, abstractmethod


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
            raise BinarySearchTreeTypeError("The root of the binary search tree can only be an element of type {0}".format(elements_type))

    def __str__(self):
        """
        the string representation of the binary search tree

        :return: a string, which contains information about the tree, such as the root value
        """

        return "Binary search tree with root: {0}".format(self.__root)

    def __repr__(self):
        repr(self.__root)

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
            raise BinarySearchTreeTypeError("The binary tree can only contain elements of type {0}".format(self.__elements_type))

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
            raise BinarySearchTreeTypeError("The binary tree only contains elements of type {0}".format(self.__elements_type))

    def delete(self, value):
        """
        this method deletes an element with a certain value from the tree

        :param value: the value to delete
        :raises BinarySearchTreeTypeError: if the type of the argument is different than the type of elements in the binary search tree
        :raises BinarySearchTreeElementError: if there is no node with the given value in the tree
        """

        if self.is_empty():
            raise BinarySearchTreeElementError("You are trying to delete an element which doesn't exist in the tree.")

        if type(value) == self.__elements_type:
            if self.__root.delete(value):
                self.__number_of_items -= 1
            else:
                raise BinarySearchTreeElementError("You are trying to delete an element which doesn't exist in the tree.")
        else:
            raise BinarySearchTreeTypeError("The binary tree only contains elements of type {0}".format(self.__elements_type))

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

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return repr(self.__value)

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


class BinaryHeap(ABC):
    """
    implementation for the Abstract Data Structure called Binary Heap, the class extends the ABC class, which makes it
    an abstract class that cannot be instantiated directly, instead you can use MinBinaryHeap and MaxBinaryHeap
    """

    def __init__(self, elements_type=int):
        """
        a constructor for the BinaryHeap class

        :param elements_type: optional argument, default value is int, only elements of this type can be added
            to the heap
        :raises BinaryHeapTypeError: if the 'elements_type' argument is specified and is not a valid type
        """

        if type(elements_type) != type:
            raise BinaryHeapTypeError("{0} is not a valid type for a binary heap.".format(elements_type))

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

    def __repr__(self):
        """
        this is the repr representation of the heap

        :return: the repr representation of the list of elements in the heap
        """

        return repr(self.__elements)

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
        :raises BinaryHeapTypeError: in case the argument's type differs from the type of elements in the heap
        """

        if type(item) == self.__elements_type:
            return item in self.__elements
        else:
            raise BinaryHeapTypeError("The binary heap contains only elements of type {0}".format(self.__elements_type))

    def add(self, element):
        """
        this method adds an element in the heap

        :param element: the element to add
        :raises BinaryHeapTypeError: if the argument's type is different from the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            self.__elements.append(element)

            self.__percolate_up()
        else:
            raise BinaryHeapTypeError("The element you are trying to add in the heap is not of type {0}".format(self.__elements_type))

    @abstractmethod
    def __percolate_up(self, initial_index=-1):
        """
        declaring this method as an abstract method requires all child classes to provide implementation
        """

        pass

    @abstractmethod
    def __percolate_down(self, initial_index=0):
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
        """

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

    def _BinaryHeap__percolate_up(self, initial_index=-1):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        it is meant to be used after the add operation
        """

        if initial_index == -1:
            initial_index = self.size() - 1

        child = initial_index

        if child < self.size():
            # find its correct place in the heap
            while child > 0:
                parent = int((child - 1)/2)
                if self.__elements[child] >= self.__elements[parent]:
                    break

                temp = self.__elements[child]
                self.__elements[child] = self.__elements[parent]
                self.__elements[parent] = temp
                child = parent

    def _BinaryHeap__percolate_down(self, initial_index=0):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        it is meant to be used after the remove_min operation
        """

        parent = initial_index
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

        if not self.is_empty():
            return self.__elements[0]
        else:
            return None

    def remove_min(self):
        """
        this method removes the minimum element from the heap

        :return: the minimum element in the heap
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        """

        if not self.is_empty():
            min_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()

            self._BinaryHeap__percolate_down()

            return min_element
        else:
            raise EmptyBinaryHeapError("There are no elements in the heap.")

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
        perform better than using remove_min() and add() for replacing the root

        :param element: the new element to replace the root
        :return: the smallest element in the heap
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        :raises BinaryHeapTypeError: if the type of the argument is different than the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise EmptyBinaryHeapError("There are no elements in the heap.")
        else:
            raise BinaryHeapTypeError("The element you are trying to add in the heap is not of type {0}".format(self.__elements_type))

    def replace(self, old_element, new_element):
        """
        this method replaces an element in the heap with a new element and adjusts the order

        :param old_element: the element to replace
        :param new_element: the new element
        :raises BinaryHeapTypeError: if the type of any of the arguments is not the same as the type of elements in the heap
        :raises BinaryHeapElementError: if the old element is not contained in the heap
        """

        if type(old_element) != self.__elements_type:
            raise BinaryHeapTypeError("The old element you are trying to replace in the heap is not of type {0}".format(self.__elements_type))

        if type(new_element) != self.__elements_type:
            raise BinaryHeapTypeError("The new element to add in the heap is not of type {0}".format(self.__elements_type))

        replaced = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == old_element:
                self.__elements[index] = new_element

                self._BinaryHeap__percolate_down(initial_index=index)
                self._BinaryHeap__percolate_up(initial_index=index)

                replaced = True
                break

        if not replaced:
            raise BinaryHeapElementError("The element you are trying to replace is not contained in the heap.")

    def remove(self, element):
        """
        this method removes an element in the heap

        :param element: the element to remove
        :raises BinaryHeapTypeError: if the type of the argument is not the same as the type of the elements in the heap
        :raises BinaryHeapElementError: if the element to remove is not contained in the heap
        """

        if type(element) != self.__elements_type:
            raise BinaryHeapTypeError("The element to remove from the heap is not of type {0}".format(self.__elements_type))

        removed = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == element:
                if self.size() == 1:
                    self.__elements.pop()
                else:
                    self.__elements[index] = self.__elements[len(self.__elements) - 1]
                    self.__elements.pop()

                    self._BinaryHeap__percolate_down(initial_index=index)
                    self._BinaryHeap__percolate_up(initial_index=index)

                removed = True
                break

        if not removed:
            raise BinaryHeapElementError("The element you are trying to remove is not contained in the heap.")


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
        """

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

        :return: the max element in the heap and removes it
        :raises StopIteration: if the heap is empty
        """

        if not self.is_empty():
            return self.remove_max()
        else:
            raise StopIteration

    def _BinaryHeap__percolate_up(self, initial_index=-1):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to be used after the add operation
        """

        if initial_index == -1:
            initial_index = self.size() - 1

        child = initial_index

        if child < self.size():
            # find its place in the heap
            while child > 0:
                parent = int((child - 1)/2)
                if self.__elements[child] <= self.__elements[parent]:
                    break

                temp = self.__elements[child]
                self.__elements[child] = self.__elements[parent]
                self.__elements[parent] = temp
                child = parent

    def _BinaryHeap__percolate_down(self, initial_index=0):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to be used after the remove_max operation
        """

        parent = initial_index
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

        if not self.is_empty():
            return self.__elements[0]
        else:
            return None

    def remove_max(self):
        """
        this method removes the maximum element from the heap

        :return: the maximum element in the heap
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        """

        if not self.is_empty():
            max_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()

            self._BinaryHeap__percolate_down()

            return max_element
        else:
            raise EmptyBinaryHeapError("There are no elements in the heap")

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
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        :raises BinaryHeapTypeError: if the type of the argument is different than the type of elements in the heap
        """

        if type(element) == self.__elements_type:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise EmptyBinaryHeapError("There are no elements in the heap")
        else:
            raise BinaryHeapTypeError("The element you are trying to add in the heap is not of type {0}".format(self.__elements_type))

    def replace(self, old_element, new_element):
        """
        this method replaces an element in the heap with a new element and adjusts the order

        :param old_element: the element to replace
        :param new_element: the new element
        :raises BinaryHeapTypeError: if the type of any of the arguments is not the same as the type of elements in the heap
        :raises BinaryHeapElementError: if the old element is not contained in the heap
        """

        if type(old_element) != self.__elements_type:
            raise BinaryHeapTypeError("The old element you are trying to replace in the heap is not of type {0}".format(self.__elements_type))

        if type(new_element) != self.__elements_type:
            raise BinaryHeapTypeError("The new element to add in the heap is not of type {0}".format(self.__elements_type))

        replaced = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == old_element:
                self.__elements[index] = new_element

                self._BinaryHeap__percolate_down(initial_index=index)
                self._BinaryHeap__percolate_up(initial_index=index)

                replaced = True
                break

        if not replaced:
            raise BinaryHeapElementError("The element you are trying to replace is not contained in the heap.")

    def remove(self, element):
        """
        this method removes an element in the heap

        :param element: the element to remove
        :raises BinaryHeapTypeError: if the type of the argument is not the same as the type of the elements in the heap
        :raises BinaryHeapElementError: if the element to remove is not contained in the heap
        """

        if type(element) != self.__elements_type:
            raise BinaryHeapTypeError("The element to remove from the heap is not of type {0}".format(self.__elements_type))

        removed = False
        for index in range(len(self.__elements)):
            if self.__elements[index] == element:
                if self.size() == 1:
                    self.__elements.pop()
                else:
                    self.__elements[index] = self.__elements[len(self.__elements) - 1]
                    self.__elements.pop()

                    self._BinaryHeap__percolate_down(initial_index=index)
                    self._BinaryHeap__percolate_up(initial_index=index)

                removed = True
                break

        if not removed:
            raise BinaryHeapElementError("The element you are trying to remove is not contained in the heap.")
