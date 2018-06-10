from DataStructures.Errors import *
from abc import ABC, abstractmethod


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

        :return: calls the size method to get the number of elements in the heap
        """

        return self.size

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

    @property
    def size(self):
        """
        this method gets the size of the heap

        :return: the number of elements in the heap
        """

        return len(self.__elements)

    @property
    def type(self):
        """
        this method gets the type of elements allowed to be added in the heap

        :return: the type of elements in the heap
        """

        return self.__elements_type

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

        if not self.size == 0:
            return self.remove_min()
        else:
            raise StopIteration

    def _BinaryHeap__percolate_up(self, initial_index=-1):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        it is meant to be used after the add operation
        """

        if initial_index == -1:
            initial_index = self.size - 1

        child = initial_index

        if child < self.size:
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

        if not self.size == 0:
            return self.__elements[0]
        else:
            return None

    def remove_min(self):
        """
        this method removes the minimum element from the heap

        :return: the minimum element in the heap
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        """

        if not self.size == 0:
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
                if self.size == 1:
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

        if not self.size == 0:
            return self.remove_max()
        else:
            raise StopIteration

    def _BinaryHeap__percolate_up(self, initial_index=-1):
        """
        this method is overridden from the abstract class, the implementation adjusts the heap in the correct order,
        meant to be used after the add operation
        """

        if initial_index == -1:
            initial_index = self.size - 1

        child = initial_index

        if child < self.size:
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

        if not self.size == 0:
            return self.__elements[0]
        else:
            return None

    def remove_max(self):
        """
        this method removes the maximum element from the heap

        :return: the maximum element in the heap
        :raises EmptyBinaryHeapError: if there are no elements in the heap
        """

        if not self.size == 0:
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
                if self.size == 1:
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
