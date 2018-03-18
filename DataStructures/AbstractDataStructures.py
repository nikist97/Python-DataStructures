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


from copy import deepcopy
from DataStructures.StackErrors import *
from DataStructures.QueueErrors import *
from DataStructures.TreeDataStructures import MaxBinaryHeap, MinBinaryHeap
from collections import deque


class Stack(object):
    """
    Implementation for the abstract data structure called Stack - follows the principle Last In First Out.
    The current implementation is just a wrapper around the python deque object with proper naming conventions and type
    checking.
    """

    def __init__(self, elements_type=None):
        """
        a constructor for a stack

        :param elements_type: optional argument, which represents the type of data in the stack (int, str, float, etc.)
             default value is None, which means that the stack can contain elements of all types,
             otherwise, it can contain only elements of the specified type
        :raises StackTypeError: in case the 'elements_type' argument is not a valid type
        """

        # checking that the elements_type argument is a valid type if passed
        if elements_type is not None and type(elements_type) != type:
            raise StackTypeError("{0} is not a valid type for a stack.".format(elements_type))

        # the elements in the stack are stored in a python deque object
        self.__elements = deque()
        self.__elements_type = elements_type

    def __str__(self):
        """
        the string representation for the stack returns the string representation of the deque object
        """

        return str(self.__elements)

    def __len__(self):
        """
        overriding this method so that the len(stack) syntax can be used, where stack is an object of type Stack

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
        overriding this method implements the next() method of the iterator so that the Stack object is iterable

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
        :raises StackTypeError: if the type of the Stack object is specified and is different from the type of the 'item'
            argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            return item in self.__elements
        else:
            raise StackTypeError("The parameter {0} is not of type {1}.".format(item, self.__elements_type))

    def is_empty(self):
        """
        this method checks if the stack is empty

        :return: True if the number of elements in the stack is 0 and False otherwise
        """

        return self.size() == 0

    def size(self):
        """
        this method gets the number of elements in the stack

        :return: the number of elements in the deque object, which contains the elements of the stack
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
        :raises StackTypeError: if the type of the Stack object is specified and is different from the type of the
            'item' argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            self.__elements.append(item)
        else:
            raise StackTypeError("The element {0} that you are trying to push is not of type {1}".format(item, self.__elements_type))

    def pop(self):
        """
        this method pops the top element out of the stack (the last pushed element in the stack)

        :return: the top element in the stack
        :raises EmptyStackError: if there are no elements in the stack
        """

        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            raise EmptyStackError("There are no elements in the stack")

    def peek(self):
        """
        this method peeks the top element of the stack, same as the pop() method,
        but without removing the element from the stack

        :return: the last pushed element in the stack or None if there are no elements in the stack
        """

        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def remove(self, element):
        """
        this method removes an element from the stack

        :param element: the element to remove from the stack
        :raises StackTypeError: if the type of the Stack object is specified and is different from the type of the 'element'
            argument used when calling this method
        :raises StackElementError: if the element to remove is not contained in the stack
        """

        if self.__elements_type is None or type(element) == self.__elements_type:
            try:
                self.__elements.remove(element)
            except ValueError:
                raise StackElementError("The element {0} that you are trying to remove is not contained in the stack.".format(element))
        else:
            raise StackTypeError("The element {0} that you are trying to remove is not of type {1}".format(element, self.__elements_type))


class Queue(object):
    """
    Implementation for the abstract data structure called Queue - follows the principle First In First Out.
    The current implementation is just a wrapper around the python deque object with proper naming conventions and type
    checking.
    """

    def __init__(self, elements_type=None):
        """
        a constructor for a Queue

        :param elements_type: optional argument, which represents the type of elements in the queue
            default value is None, which means that the queue can contain elements of all types,
            otherwise, the queue can only contain elements of the specified type
        :raises QueueTypeError: if the 'elements_type' argument is specified and is not a valid type
        """

        # checking that the elements_type argument is a valid type if passed
        if elements_type is not None and type(elements_type) != type:
            raise QueueTypeError("{0} is not a valid type.".format(elements_type))

        self.__elements = deque()  # elements in the queue are stored in a deque object
        self.__elements_type = elements_type

    def __str__(self):
        """
        the string representation of a queue object

        :return: the string representation of the python deque object with the elements in the queue
        """

        return str(self.__elements)

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
        :raises QueueTypeError: if the queue has a type of elements specified that is different from the type of the 'item'
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            return item in self.__elements
        else:
            raise QueueTypeError("The parameter {0} is not of type {1}.".format(item, self.__elements_type))

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

        return len(self.__elements)

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
        :raises QueueTypeError: if the type of elements in the queue is specified and is different from the type
            of the 'item' argument used when calling this method
        """

        if self.__elements_type is None or type(item) == self.__elements_type:
            self.__elements.append(item)
        else:
            raise QueueTypeError("The element {0} that you are trying to enqueue is not of type {1}".format(item, self.__elements_type))

    def dequeue(self):
        """
        this method removes the item that got first in the queue

        :raises EmptyQueueError: if there are no elements in the queue
        """

        if self.size() > 0:
            return self.__elements.popleft()
        else:
            raise EmptyQueueError("There are no elements in the queue")

    def peek(self):
        """
        this method peeks the item that got first in the queue (without removing it)

        :return: the peeked item or None if there are no elements in the queue
        """

        if self.size() > 0:
            return self.__elements[0]
        else:
            return None

    def remove(self, element):
        """
        this method removes an element from the queue

        :param element: the element to remove from the queue
        :raises QueueTypeError: if the type of elements in the queue is specified and is different from the type
            of the 'element' argument used when calling this method
        :raises QueueElementError: if the element to remove is not contained in the queue
        """

        if self.__elements_type is None or type(element) == self.__elements_type:
            try:
                self.__elements.remove(element)
            except ValueError:
                raise QueueElementError("The element {0} that you are trying to remove is not contained in the queue.".format(element))
        else:
            raise QueueTypeError("The element {0} that you are trying to remove is not of type {1}.".format(element, self.__elements_type))


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


class Graph(object):
    """
    Abstract Data Structure - represents a graph, which can be directed, oriented and weighted
    """

    def __init__(self, elements_type=None, directed=False, oriented=False, weighted=False):
        """
        a constructor for the graph
        :param elements_type: the type of elements that can be added in the graph, if set to None all types allowed
        :param directed: boolean if the graph is directed
        :param oriented: boolean if the graph is oriented
        :param weighted: boolean if the graph is weighted
        :raises TypeError: if elements_type is not a valid type
        :raises TypeError: if type of directed, oriented or weighted is not boolean
        :raises ValueError: if the graph is set to be oriented but not directed
        """

        if elements_type is not None and type(elements_type) != type:
            raise TypeError(str(elements_type) + " is not a valid type")

        if type(directed) != bool or type(oriented) != bool or type(weighted) != bool:
            raise TypeError("Type of the directed, oriented, and weighted arguments must be boolean")

        self.__elements_type = elements_type

        if oriented and not directed:
            raise ValueError("A graph cannot be oriented and not directed at the same time")

        self.__directed = directed
        self.__oriented = oriented
        self.__weighted = weighted
        self.__nodes_set = set()
        self.__nodes_list = []
        self.__edges = []

        # initialize the edges with a number of None elements
        for i in range(5):
            none_list = []
            for j in range(5):
                none_list.append(None)
            self.__edges.append(none_list)

    def __len__(self):
        """
        overriding this method allows the len(graph) syntax
        :return: the number of elements in the graph
        """

        return self.size()

    def __str__(self):
        """
        the string representation of the graph
        :return: a formatted string with basic information about the graph
        """

        return "Graph: directed - " + str(self.__directed) + ", oriented - " + str(self.__oriented) + \
               ", weighted - " + str(self.__weighted)

    def __iter__(self):
        """
        overriding this method allows the use of an iterator
        :return: the iterator of the list of nodes in the graph
        """

        return iter(self.__nodes_list)

    def __contains__(self, item):
        """
        overriding this method allows the use of the 'element in graph' syntax
        :param item: the node to search for
        :return: True if the node is contained in the graph and False otherwise
        """

        return self.contains(item)

    def size(self):
        """
        this method gets the size of the graph
        :return: the number of nodes in the graph
        """

        return len(self.__nodes_set)

    def is_empty(self):
        """
        this method checks if the graph is empty
        :return: True if there are no nodes in the graph and False otherwise
        """

        return self.size() == 0

    def type(self):
        """
        a getter method for the type of elements in the graph
        :return: the type of nodes in the graph or None if all types allowed
        """

        return self.__elements_type

    def is_weighted(self):
        """
        checks if the graph is weighted
        :return: True if the graph is weighted and False otherwise
        """

        return self.__weighted

    def is_oriented(self):
        """
        checks if the graph is oriented
        :return: True if the graph is oriented and False otherwise
        """

        return self.__oriented

    def is_directed(self):
        """
        checks if the graph is directed
        :return: True if the graph is directed and False otherwise
        """

        return self.__directed

    def contains(self, item):
        """
        this method checks if a node exists in the graph
        :param item: the node to search for
        :return: True if the node is contained in the graph and False otherwise
        :raises TypeError: if the type of item is not the same as the type of elements in the graph
        """

        if self.__elements_type is not None and type(item) != self.__elements_type:
            raise TypeError("The item you are trying to find is not of type " + str(self.__elements_type))

        return item in self.__nodes_set

    def contains_edge(self, first_item, second_item):
        """
        this method checks if an edge from the first_item to the second_item exists
        :param first_item: the starting node
        :param second_item: the target node
        :return: True if an edge exists and False otherwise
        :raises TypeError: if the arguments' type is not the same as the type of elements in the graph
        :raises KeyError: if one or both of the arguments are not contained in the graph
        """

        if self.__elements_type is not None and type(first_item) != self.__elements_type:
            raise TypeError("The first argument is not of type " + str(self.__elements_type))

        if self.__elements_type is not None and type(second_item) != self.__elements_type:
            raise TypeError("The second argument is not of type " + str(self.__elements_type))

        if first_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the first argument")

        if second_item not in self.__nodes_set:
            raise KeyError("The graph doesn't contain the second argument")

        return self.__edges[self.__nodes_list.index(first_item)][self.__nodes_list.index(second_item)] is not None

    def get_edge_weight(self, first_item, second_item):
        """
        a getter method for the weight of an edge between two nodes
        :param first_item: the start node
        :param second_item: the target node
        :return: the weight of the edge
        :raises TypeError: if the type of the arguments is not the same as the type of the nodes in the graph
        :raises KeyError: if the graph doesn't contain the argument nodes
        :raises ValueError: if the graph is not weighted
        :raises ValueError: if the edge doesn't exist
        """

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

    def nodes(self):
        """
        a getter method for the nodes of the graph
        :return: a deep copy of the list with nodes objects so that the original list containing the nodes of the graph
            is not manually altered by the user
        """

        return deepcopy(self.__nodes_list)

    def edges(self):
        """
        a getter method for the edges of the graph
        :return: a deep copy of the list with edges so that the original list containing the edges in the graph is not
            manually altered
        """

        return deepcopy(self.__edges)

    def edges_of(self, item):
        """
        this method gets all ages for a single node
        :param item: the start node
        :return: a list of nodes linked to the argument node with an edge
        """

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

    def add_node(self, item):
        """
        this method adds a node in the graph
        :param item: the value of the node
        :raises TypeError: if the value's type is not the same as the other nodes in the graph
        :raises AttributeError: if the item to add is None
        """

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

    def remove_node(self, item):
        """
        this method removes a node from the graph
        :param item: the value of the node to remove
        :raises TypeError: if the type of the node is not the same as the type of the other nodes in the graph
        :raises KeyError: if the node is not contained in the graph
        """

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

    def add_edge(self, first_item, second_item, edge_weight=None):
        """
        this method adds an edge between two nodes in the graph
        :param first_item: the start node
        :param second_item: the target node
        :param edge_weight: (optional argument) the weight of the edge if appropriate
        :raises TypeError: if the start or the target node's type is not the same as the type of the other nodes
        :raises TypeError: if the edge weight is set and is not of type float or int
        :raises KeyError: if the graph doesn't contain any of the nodes
        :raises ValueError: if the graph is weighted and weight is not given by argument
        :raises KeyError: if the graph is oriented and an edge with the oposite direction already exists
        """

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

    def remove_edge(self, first_item, second_item):
        """
        this method removes an edge in the graph
        :param first_item: the start node
        :param second_item: the target node
        :raises TypeError: if the type of the nodes is not the same as the type of the other nodes in the graph
        :raises KeyError: if the graph doesn't contain any of the nodes
        :raises KeyError: if there is no edge between the given nodes
        """

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

    def replace_node(self, old_node, new_node):
        """
        replaces an old node with a new node by not removing the old node's edges, instead they are now linked to the
        new node
        :param old_node: the old node
        :param new_node: the new node
        :raises TypeError: if the type of the nodes is not the same as the other nodes in the graph
        :raises KeyError: if the graph doesn't contain the old node
        :raises KeyError: if the graph already contains the new node
        """

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
