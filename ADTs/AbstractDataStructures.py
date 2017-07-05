from abc import ABC, abstractmethod


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

    # iterator method
    def __iter__(self):
        return self

    # next method for iterator
    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.pop()

    # the 'item in stack' method
    def __contains__(self, item):
        return self.contains(item)

    # the contains method, which checks if an item is in the stack
    def contains(self, item):
        if self.__elementsType is None or type(item) == self.__elementsType:
            return item in self.__elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elementsType))

    # the is_empty method, which checks if the size of the stack is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the stack
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the stack elements
    def type(self):
        return self.__elementsType

    # the push method, which pushes an item into the stack, raises a TypeError if elementType is not None,
    # but different from the parameter item's type
    def push(self, item):
        if self.__elementsType is None or type(item) == self.__elementsType:
            self.__elements.append(item)
        else:
            raise TypeError("The element you are trying to push is not of type " + str(self.__elementsType))

    # the pop method, which takes out the last element that got into the stack;
    # it raises a ValueError if there is no element to pop (if size of the stack is 0)
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            raise ValueError("There are no elements in the stack")

    # the peek method, which returns the last element that got into the stack, but doesn't remove it from the stack;
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

    # iterator implementation
    def __iter__(self):
        return self

    # the next method for the iterator
    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.dequeue()

    # the 'item in queue' method
    def __contains__(self, item):
        return self.contains(item)

    # the contains method which checks if an item is in the queue
    def contains(self, item):
        if self.__elementsType is None or type(item) == self.__elementsType:
            return item in self.__elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elementsType))

    # the is_empty method, which checks if the size of the queue is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the queue
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the queue elements
    def type(self):
        return self.__elementsType

    # the enqueue method, which inserts an item into the queue, raises a TypeError if elementsType is not None and is
    # different than the parameter item's type
    def enqueue(self, item):
        if self.__elementsType is None or type(item) == self.__elementsType:
            self.__elements.append(item)
        else:
            raise TypeError("The element you are trying to enqueue is not of type " + str(self.__elementsType))

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


# Abstract Data Type Binary Search Tree
class BinarySearchTree(object):

    # the constructor for the binary tree, it has a root as an optional argument, if the root is specified the tree
    # is initialised with a root, else it is initialized with no root, the elements in the tree must be from the type
    # specified in the constructor, the default type that is used is int
    def __init__(self, root=None, elements_type=int):
        # variables used for the iterator of the binary tree
        self.__successor = None
        self.__iterator_limit = None
        self.__iterator_finished = None
        self.__current_item = None

        if elements_type is None:
            elements_type = int
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

    # string representation of the binary search tree
    def __str__(self):
        if self.__root is not None:
            return "Binary search tree with root: " + str(self.__root.get_value())
        else:
            return "Binary search tree with root: None"

    # overriding the __contains__ method
    def __contains__(self, item):
        return self.contains(item)

    # overriding the __len__ method
    def __len__(self):
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

    # the add method, which adds a Node with the value given as an argument to the binary search tree
    def add(self, value):
        if type(value) == self.__elements_type:
            if self.__root is None or self.__root.get_value() is None:
                self.__root = Node(value)
                self.__number_of_items = 1
            else:
                if self.__root.add(Node(value)):
                    self.__number_of_items += 1
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    # the contains method, which finds if an element exists in the binary tree
    def contains(self, value):
        if type(value) == self.__elements_type:
            return self.__root.contains(value)
        else:
            raise TypeError("The binary tree can contain only elements of type " + str(self.__elements_type) + ".")

    # the delete method, which deletes an element from the tree
    def delete(self, value):
        if type(value) == self.__elements_type:
            self.__root.delete(value)
            self.__number_of_items -= 1
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

        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node.get_value()

    # a getter method for the minimum element in the tree, this one returns the Node element rather than just the value,
    # used for the iterator
    def __get_minimum_node(self):
        current_node = self.__root

        if current_node is None:
            return None

        # go left as much as possible to find the minimum element
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node

    # a getter method for the maximum element in the tree
    def get_maximum(self):
        current_node = self.__root

        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node.get_value()

    # a getter method for the maximum element in the tree, this one returns the Node element rather than just the value,
    # used for the iterator
    def __get_maximum_node(self):
        current_node = self.__root

        # if the root is None, return None
        if current_node is None:
            return None

        # go right as much as possible to find the maximum element
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node


# the Node class, which represents a Node in the binary search tree
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
        if node is None or type(node) == Node:
            self.__left = node
        else:
            raise TypeError("The child of a node must be a node.")

    # a getter method for the right child
    def get_right(self):
        return self.__right

    # a setter method for the right child
    def set_right(self, node=None):
        if node is None or type(node) == Node:
            self.__right = node
        else:
            raise TypeError("The child of a node must be a node.")

    # a getter method for the parent of the node
    def get_parent(self):
        return self.__parent

    # a setter method for the parent of the node
    def set_parent(self, node=None):
        if node is None or type(node) == Node:
            self.__parent = node
        else:
            raise TypeError("The parent of a node must be a node.")

    # the add method, which adds a node to the current node as a child,
    # the method returns a boolean representing whether the tree has added an element or not
    def add(self, node):
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

    # the delete method of the Node class, which deletes a node
    def delete(self, value):
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
        if type(node) == Node:
            self.__left = node
            self.__left.set_parent(self)
        else:
            raise TypeError("You can only add a Node as a left child.")

    def __add_right(self, node):
        if type(node) == Node:
            self.__right = node
            self.__right.set_parent(self)
        else:
            raise TypeError("You can only add a Node as a right child.")


# Abstract Data Type BinaryHeap, abstract class - can't be instantiated, use MinBinaryHeap or MaxBinaryHeap
class BinaryHeap(ABC):

    # constructor for binary heap, optional argument elements_type (it's set to int if not provided)
    # the elements in the binary heap must be from the type specified in the constructor,
    # the default type that is used is int
    def __init__(self, elements_type=int):
        self.__elements = []
        self.__elementsType = elements_type

    # the len(heap) method
    def __len__(self):
        return self.size()

    # the str(heap) method
    def __str__(self):
        return str(self.__elements)

    # the 'item in priority queue' method
    def __contains__(self, item):
        return self.contains(item)

    @abstractmethod
    # overriding the __iter__ method, so that we can go through the elements of the heap
    def __iter__(self):
        pass

    @abstractmethod
    # overriding the __next__ method, so that we can use the iterator
    def __next__(self):
        pass

    # the is_empty method, which checks if the size of the heap is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the heap
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the heap elements
    def type(self):
        return self.__elementsType

    # the contains method, which checks if an element is in the heap
    def contains(self, item):
        if type(item) == self.__elementsType:
            return item in self.__elements
        else:
            raise TypeError("The parameter is not of type " + str(self.__elementsType))

    # the add method, which adds an element to the heap
    def add(self, element):
        if type(element) == self.__elementsType:
            self.__elements.append(element)

            self.__percolate_up()
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elementsType))

    # the percolate_up method which adjusts the heap after an addition operation,
    # it gets the last element in the list and finds its place in the heap
    @abstractmethod
    def __percolate_up(self):
        pass

    @abstractmethod
    # the percolate_down method, which adjusts the heap after a remove_min operation,
    # it starts with the first element in the list and finds its place in the heap
    def __percolate_down(self):
        pass

    @abstractmethod
    # the get_sorted_elements method, which returns the sorted elements of the heap
    def get_sorted_elements(self):
        pass

    @abstractmethod
    # the replace_root method, runs faster than remove_min/remove_max followed by add
    def replace_root(self, element):
        pass


# Abstract Data Type MinBinaryHeap - represents a BinaryHeap with a root its minimum element
# noinspection PyAbstractClass,PyPep8Naming
class MinBinaryHeap(BinaryHeap):

    # constructor for MinBinaryHeap, same arguments as abstract BinaryHeap class
    def __init__(self, elements_type=int):
        if elements_type is None:
            elements_type = int
        BinaryHeap.__init__(self, elements_type)

        self.__elements = self._BinaryHeap__elements
        self.__elementsType = self._BinaryHeap__elementsType

    # iterator goes through the sorted elements starting from the min entry
    def __iter__(self):
        return self

    # overriding the next method in order to use the iterator
    def __next__(self):
        if not self.is_empty():
            return self.remove_min()
        else:
            raise StopIteration

    # the percolate_up method which adjusts the heap after an addition operation,
    # it gets the last element in the list and finds its place in the heap
    def _BinaryHeap__percolate_up(self):
        child = len(self.__elements) - 1

        while child > 0:
            parent = int((child - 1)/2)
            if self.__elements[child] >= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp
            child = parent

    # the percolate_down method, which adjusts the heap after a remove_min operation,
    #  it gets the first element in the list and finds its place in the heap
    def _BinaryHeap__percolate_down(self):
        parent = 0
        child = 2*parent + 1

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

    # the peek_min method, which returns the minimum element in the heap, but doesn't remove it,
    # returns None if no elements in the heap
    def peek_min(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    # the remove_min method, which removes and returns the minimum element in the heap,
    # raises a ValueError if there are no elements in the heap
    def remove_min(self):
        if len(self.__elements) > 0:
            min_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()
            self._BinaryHeap__percolate_down()

            return min_element
        else:
            raise ValueError("There are no elements in the heap")

    # returns the sorted elements in the heap starting from the minimum entry
    def get_sorted_elements(self):
        temp_elements = [k for k in self.__elements]
        sorted_elements = []

        while len(self.__elements) > 0:
            sorted_elements.append(self.remove_min())

        self.__elements = temp_elements
        # noinspection PyAttributeOutsideInit
        self._BinaryHeap__elements = temp_elements

        return sorted_elements

    # removes and returns the smallest item in the heap and adds the new item, faster than remove_min followed by add
    def replace_root(self, element):
        if type(element) == self.__elementsType:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise ValueError("There are no elements in the heap")
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elementsType))


# Abstract Data Type MaxBinaryHeap - represents a BinaryHeap with a root its maximum element
# noinspection PyAbstractClass,PyPep8Naming
class MaxBinaryHeap(BinaryHeap):

    # constructor for MaxBinaryHeap, same arguments as abstract BinaryHeap class
    def __init__(self, elements_type=int):
        if elements_type is None:
            elements_type = int
        BinaryHeap.__init__(self, elements_type)

        self.__elements = self._BinaryHeap__elements
        self.__elementsType = self._BinaryHeap__elementsType

    # iterator goes through the sorted elements starting from the max entry
    def __iter__(self):
        return iter(self.get_sorted_elements())

    # overriding the next method in order to use the iterator
    def __next__(self):
        if not self.is_empty():
            return self.remove_max()
        else:
            raise StopIteration

    # the percolate_up method which adjusts the heap after an addition operation,
    # it gets the last element in the list and finds its place in the heap
    def _BinaryHeap__percolate_up(self):
        child = len(self.__elements) - 1

        while child > 0:
            parent = int((child - 1)/2)
            if self.__elements[child] <= self.__elements[parent]:
                break

            temp = self.__elements[child]
            self.__elements[child] = self.__elements[parent]
            self.__elements[parent] = temp
            child = parent

    # the percolate_down method, which adjusts the heap after a remove_max operation,
    #  it gets the first element in the list and finds its place in the heap
    def _BinaryHeap__percolate_down(self):
        parent = 0
        child = 2*parent + 1

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

    # the peek_max method, which returns the maximum element in the heap, but doesn't remove it,
    # returns None if no elements in the heap
    def peek_max(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    # the remove_max method, which removes and returns the maximum element in the heap,
    # raises a ValueError if there are no elements in the heap
    def remove_max(self):
        if len(self.__elements) > 0:
            max_element = self.__elements[0]

            self.__elements[0] = self.__elements[len(self.__elements) - 1]
            self.__elements.pop()
            self._BinaryHeap__percolate_down()

            return max_element
        else:
            raise ValueError("There are no elements in the heap")

    # returns the sorted elements in the heap starting from the maximum entry
    def get_sorted_elements(self):
        temp_elements = [k for k in self.__elements]
        sorted_elements = []

        while len(self.__elements) > 0:
            sorted_elements.append(self.remove_max())

        self.__elements = temp_elements
        # noinspection PyAttributeOutsideInit
        self._BinaryHeap__elements = temp_elements

        return sorted_elements

    # removes and returns the maximum item in the heap and adds the new item, faster than remove_max followed by add
    def replace_root(self, element):
        if type(element) == self.__elementsType:
            if len(self.__elements) > 0:
                temp = self.__elements[0]
                self.__elements[0] = element
                self._BinaryHeap__percolate_down()
                return temp
            else:
                raise ValueError("There are no elements in the heap")
        else:
            raise TypeError("The element you are trying to add is not of type " + str(self.__elementsType))


# Abstract Data Type PriorityQueue
class PriorityQueue(object):

    # constructor for the priority queue;
    # elements_type denotes the type of elements that can be added to the priority queue, default is None, which allows
    # all types of elements to be added to queue;
    # reverse denotes a boolean, which represents what kind of priority queue to use, if set to False(default), then the
    # element with greatest priority will be returned by dequeue, if set to True - it returns the element with minimum
    # priority when using  dequeue
    def __init__(self, elements_type=None, reverse=False):

        if not reverse:
            self.__indices = MaxBinaryHeap(int)
        else:
            self.__indices = MinBinaryHeap(int)

        self.__elements = {}
        self.__elements_type = elements_type

    # the string representation for the priority queue returns the elements of the priority queue
    def __str__(self):
        return str(self.__elements)

    # the len(priority_queue) method
    def __len__(self):
        return self.size()

    # the 'item in priority queue' method
    def __contains__(self, priority):
        return self.contains(priority)

    # iterator implementation
    def __iter__(self):
        return self

    # the next method used for the iterator
    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.dequeue()

    # the is_empty method, which checks if the size of the priority queue is 0
    def is_empty(self):
        return len(self.__elements) == 0

    # the size method, which returns the size of the priority queue
    def size(self):
        return len(self.__elements)

    # the type method, which returns the type of the priority queue elements
    def type(self):
        return self.__elements_type

    def is_reversed(self):
        return type(self.__indices) == MinBinaryHeap

    # the enqueue method, which inserts an item into the queue with a given priority, raises a TypeError if
    # elements_type is not None and is different than the parameter item's type;
    # raises a TypeError if the type of the parameter priority is not int;
    # if the priority parameter already exists in the queue, the element stored with this priority will be overwritten
    # by the new element
    def enqueue(self, item, priority):
        if type(priority) != int:
            raise TypeError("The priority must be an integer")

        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The element you are trying to enqueue is not of type " + str(self.__elements_type))

        if priority not in self.__elements:
            self.__indices.add(priority)
        self.__elements[priority] = item

    # the dequeue method, which takes the element with the greatest or the lowest priority depending on the reverse
    # argument in the constructor, then removes it from the priority queue and returns it;
    # raises a ValueError if there are no elements in the priority queue
    def dequeue(self):
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

    # same as dequeue but doesn't remove the element from the priority queue and just returns it;
    # returns None if there are no elements in the queue
    def peek(self):
        if self.is_empty():
            return None

        if type(self.__indices) == MinBinaryHeap:
            return self.__elements.get(self.__indices.peek_min())
        elif type(self.__indices) == MaxBinaryHeap:
            return self.__elements.get(self.__indices.peek_max())

    # get the element with the specified priority,
    # returns None if no element with this priority exists,
    # raises a TypeError if the parameter is not an integer
    def get(self, priority):
        if type(priority) != int:
            raise TypeError("The priority parameter must be an integer.")

        return self.__elements.get(priority)

    # the contains method, which checks if a given priority is assigned to an object
    def contains(self, priority):
        if type(priority) == int:
            return priority in self.__elements.keys()
        else:
            raise TypeError("Priorities must be of type int")

    # the contains_element method checks if a given element is contained in the queue
    def contains_element(self, element):
        if self.__elements_type is not None and type(element) != self.__elements_type:
            raise TypeError("Type of the parameter is not " + self.__elements_type)

        return element in self.__elements.values()
