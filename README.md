# Abstract Data Structures and Algorithms-Python

**_The repository contains implementations for some of the most famous data structures, algorithms and applications of those algorithms_**

Navigate to [stack](#stack)

### Abstract Data Structures in Python

**_Implementation for Stack, Queue, Binary Search Tree, Max Binary Heap, Min Binary Heap, Priority Queue and 
Graph in Python_** <br>
**All of these are located in the AbstractDataStructures.py module** <br><br>

- **_Stack<a name="stack"></a> (First-In-Last-Out)_** <br>
The Stack's implementation is generic: you can specify the type of elements in the stack in the constructor.
If not specified, it is set to None and elements of any type can be added to the stack. The
implementation includes all the common operations of a stack: peek, push, pop, size, etc.<br>

_API_ :
```python
from ADTs.AbstractDataStructures import Stack # import the stack data structure

stack = Stack() # type is set to None, items of any types can be added
stack = Stack(elements_type = int) # type is set to int, hence only integers can be pushed

stack.size() # returns the number of elements in the stack
len(stack) # same as stack.size()
stack.is_empty() # returns True if stack is empty and False otherwise

str(stack) # returns the string representation of the list of elements of the stack

item = "test_item"
stack.contains(item) # returns True if the item is in the stack and False otherwise
# contains raises a TypeError if the type of the stack is not None and is different 
# than the type of the parameter
boolean = item in stack 
# same as boolean = stack.contains(item)

stack.type() # returns the type of the elements in the stack, None if no type is specified

stack.peek() # returns the last element that was added to the stack, but doesn't remove it
# peek returns None if there are no elements in the stack

stack.pop() # same as peek(), but removes the last element that was added to the stack
# pop raises a ValueError if there are no elements in the stack

element = "test_item"
stack.push(element) # pushes the element to the top of the stack
# push raises a TypeError if the stack has a specified type for elements
# and the argument is not of that type

# the implemenetation includes an iterator
for element in stack:
    print(element)
# keep in mind that the iterator uses stack.pop() to get the next element, hence
# after the iteration is over the stack would be empty
```

<br> <br>

- **_Queue (First-In-First-Out)_** <br>
The Queue's implementation is generic: you can specify the type of elements in the queue in the constructor.
If not specified, it is set to None and elements of any type can be added to the queue. The
implementation includes all the common operations of a queue: enqueue, dequeue, peek, size, etc.<br>

_API_ :
```python
from ADTs.AbstractDataStructures import Queue # import the queue data structure
queue = Queue() # type is set to None, items of any types can be added
queue = Queue(elements_type = str) # type is set to str, hence only strings can be enqueued

queue.size() # returns the number of elements in the queue
len(queue) # same as queue.size()
queue.is_empty() # return True if queue is empty and False otherwise

str(queue) # return the string representation of the list of elements of the queue

item = "test_item"
queue.contains(item) # returns True if the item is in the queue and False otherwise
# contains raises a TypeError if the type of the queue is not None and is different 
# than the type of the parameter
boolean = item in queue 
# same as boolean = queue.contains(item)

queue.type() # returns the type of the elements in the queue, None if no type is specified

queue.peek() # returns the first element that was added to the queue, but doesn't remove it
# peek returns None if there are no elements in the queue

queue.dequeue() # same as peek(), but removes the first element that was added to the queue
# dequeue raises a ValueError if there are no elements in the queue

element = "test_element"
queue.enqueue(element) # enqueues the element to the back of the queue
# enqueue raises a TypeError if the queue has a specified type for elements
# and the argument is not of that type

# the implemenetation includes an iterator
for element in queue:
    print(element)
# keep in mind that the iterator uses queue.dequeue() to get the next element, hence
# after the iteration is over the queue would be empty
```


<br> <br>

- **_Binary Search Tree_** <br>
The Binary Search Tree's implementation is generic: you can specify the type of elements in the binary search tree
in the constructor. If not specified, it is set to int, hence only integers can be added to the binary search tree.
You can also initiate the root of the tree by specifying it in the constructor. If not specified a binary search tree
with no root is created and the first added element becomes the root. The implementation includes all the common
operations of a binary search tree: contains, add, delete, get_maximum, get_minimum, etc.<br>

_API_ :
```python
from ADTs.AbstractDataStructures import BinarySearchTree # import the BinarySearchTree data structure

tree = BinarySearchTree() # type is set to default - int, hence only integers can be added,
# creates an empty tree with no root

tree = BinarySearchTree(elements_type = str) # type is set to str, hence only strings can be added
# creates an empty tree with no root

tree = BinarySearchTree(root = 10) # type is set to default - int, hence only integers can be added
# creates a tree with the argument value as a root, raises a TypeError if argument for root is not int

tree = BinarySearchTree(root = "man", elements_type = str) # type is set to str, hence only strings
# can be added, creates a tree with the argument value as a root, raises a TypeError if argument is
# not of the type specified in the constructor

tree.get_number_of_elements() # returns the number of elements in the tree
len(tree) # same as tree.get_number_of_elements()
tree.is_empty() # returns True if the tree is empty and False otherwise

str(tree) # returns a string in the format Binary search tree with root 'root'

tree.type() # returns the type of the elements in the binary search tree

element = "test_element"
tree.contains(element) # returns true if the element exists in the binary search tree
# contains raises a TypeError if the type of the argument is not the same as the type of the elements in the tree

boolean = element in tree # same as boolean = tree.contains(element)

tree.add(element) # adds the element to the binary tree on the place it should be located
# add raises a TypeError if the type of the argument is not the same as the type of the elements in the tree

tree.delete(element) # deletes the element from the binary tree if the tree contains it
# delete raises a TypeError if the type of the argument is not the same as the type of the elements in the tree
# delete raises a KeyError if the element is not contained in the binary tree

tree.get_minimum() # returns the minimum element in the binary search tree
# returns None if number of elements is 0

tree.get_maximum() # returns the maximum element in the binary search tree
# returns None if number of elements is 0

tree.get_root() # returns the root element in the binary search
# returns None if number of elements is 0

# the tree also implements an iterator, which goes through all the elements in the tree in order
# starting from the minimum element
for element in tree:
    print(element)
```


<br> <br>

- **_BinaryHeap_** <br>
The BinaryHeap's implementation is generic: you can specify the type of elements in the heap in the constructor. If not 
specified, it is set to int, hence only integers can be added to the heap. The BinaryHeap class is abstract. You cannot 
instantiate it. The implementation includes two types of heaps, which you can use: MinBinaryHeap and MaxBinaryHeap.
<br>

**MinBinaryHeap** - a heap with its root being the minimum element <br>
MinBinaryHeap implements the common operations of a heap: add, replace_root, remove_min, peek_min, size, etc.

<br>

**MaxBinaryHeap** - a heap with its root being the maximum element <br>
MaxBinaryHeap implements the common operations of a heap: add, replace_root, remove_max, peek_max, size, etc.

<br>

MinBinaryHeap _API_ : 
```python
from ADTs.AbstractDataStructures import MinBinaryHeap # import the min heap

min_heap = MinBinaryHeap() # type is set to default - int, hence only integers can be added
# creates an empty heap

min_heap = MinBinaryHeap(str) # type is set to str, hence only strings can be added
# creates an empty heap

min_heap.size() # returns the number of elements in the heap
len(min_heap) # same as min_heap.size()
min_heap.is_empty() # returns True if the heap doesn't have elements and False otherwise

str(min_heap) # returns a string of the list of elements in the heap

min_heap.type() # returns the type of elements in the heap

element = "test_element"
min_heap.add(element) # adds the element to the min binary heap on the place it should be located
# add raises a TypeError if the type of the argument is not the same as the type of the elements in the heap

min_heap.peek_min() # returns the minimum element (the root), but doesn't remove it from the heap
# returns None if heap is empty

min_heap.remove_min() # returns the minimum element (the root) and removes it from the heap
# the method replaces the root with the second minimum element in the heap
# it raises a ValueError if the heap is empty

# returns the minimum element (the root) and removes it from the heap, by replacing it with the element argument
min_heap.replace_root(element) 
# same as min_heap.remove_min() followed by min_heap.add(element), but replace_root() is faster
# raises a TypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a ValueError if the heap is empty

min_heap.get_sorted_elements() # returns a list with the sorted elements from the heap, the heap remains unchanged
# the order is ascending; returns an empty list if the heap is empty

# the iterator goes through each element in the heap in ascending order
for element in min_heap:
    print(element)
# keep in mind that using the iterator will remove each element you go through from the heap, since it uses remove_min()
# to generate the next element, hence when the iterator is finished the heap would be empty;
# if you want to keep the elements in the heap, use get_sorted_elements() (although it's slightly slower)

# another example with the iterator
heap_iter = iter(min_heap)
while True:
    try:
        print(heap_iter.__next__())
    except StopIteration:
        break
min_heap.size() # will return 0 after iteration is finished, as explained above
```

<br>

MaxBinaryHeap _API_:
```python
from ADTs.AbstractDataStructures import MaxBinaryHeap # import the max heap

max_heap = MaxBinaryHeap() # type is set to default - int, hence only integers can be added
# creates an empty heap

max_heap = MaxBinaryHeap(str) # type is set to str, hence only strings can be added
# creates an empty heap

max_heap.size() # returns the number of elements in the heap
len(max_heap) # same as max_heap.size()
max_heap.is_empty() # returns True if the heap doesn't have elements and False otherwise

str(max_heap) # returns a string of the list of elements in the heap

max_heap.type() # returns the type of elements in the heap

element = "test_element"
max_heap.add(element) # adds the element to the max binary heap on the place it should be located
# add raises a TypeError if the type of the argument is not the same as the type of the elements in the heap

max_heap.peek_max() # returns the maximum element (the root), but doesn't remove it from the heap
# returns None if heap is empty

max_heap.remove_max() # returns the maximum element (the root) and removes it from the heap
# the method replaces the root with the second maximum element in the heap
# it raises a ValueError if the heap is empty

# returns the maximum element (the root) and removes it from the heap, by replacing it with the element argument
max_heap.replace_root(element) 
# same as max_heap.remove_max() followed by max_heap.add(element), but replace_root() is faster
# raises a TypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a ValueError if the heap is empty

max_heap.get_sorted_elements() # returns a list with the sorted elements from the heap, the heap remains unchanged
# the order is descending; returns an empty list if the heap is empty

# the iterator goes through each element in the heap in descending order
for element in max_heap:
    print(element)
# keep in mind that using the iterator will remove each element you go through from the heap, since it uses remove_max()
# to generate the next element, hence when the iterator is finished the heap would be empty;
# if you want to keep the elements in the heap, use get_sorted_elements() (although it's slightly slower)

# another example with the iterator
heap_iter = iter(max_heap)
while True:
    try:
        print(heap_iter.__next__())
    except StopIteration:
        break
max_heap.size() # will return 0 after iteration is finished, as explained above
```


<br> <br>

- **_Priority Queue_** <br>
The Priority Queue's implementation is generic: you can specify the type of elements in the queue in the constructor. 
If not specified, it is set to None, hence objects of all types can be added to the priority queue. You can also set the reverse
argument in the constructor. If reverse is set to False (default) the queue dequeues the element with the greatest priority, 
else if the reverse argument is set to True - it dequeues the element with the lowest priority. The implementation includes 
all the common operations of a priority queue: enqueue, dequeue, peek, size, etc.<br>

_API_ :
```python
from ADTs.AbstractDataStructures import PriorityQueue # import the priority queue data structure

priority_queue = PriorityQueue() # type is set to default None, hence objects of all types can be enqueued to the queue
# the reverse argument is set to default False, hence dequeue returns the element with the highest priority

priority_queue = PriorityQueue(elements_type=str, reverse=True) # type is set to str, hence only strings can be enqueued
# the reverse argument is set to True, hence dequeue returns the element with the lowest priority

priority_queue.size() # returns the number of elements in the queue
len(priority_queue) # same as priority_queue.size()
priority_queue.is_empty() # returns True if there are no elements in the queue and False otherwise


str(priority_queue) # returns a string of the dictionary linking prioriies with elements in the queue

priority_queue.type() # returns the type of elements that can be enqueued in the priority queue
# if this method returns None, objects of all types can be enqueued

priority_queue.is_reversed() # returns True if the queue dequeues the element with the lowest priority
# returns False if the queue dequeues the element with the highest priority

priority = 10
priority_queue.contains(priority) # returns True if the queue has an element, linked to the given priority and False otherwise
# contains raises a TypeError if type of priority is not int
boolean = priority in priority_queue # same as priority_queue.contains(priority)

element = "test_element"
priority_queue.contains_element(element) # returns True if an element is contained in the queue
# raises TypeError if priority_queue.type() is not None and is different than the type of the given element

item = "test_item"
priority_queue.enqueue(item, priority) # enqueues the given item and links it the given priority
# raises TypeError if type(priority) is not int
# raises TypeError if priority_queue.type() is not None and is different than the type of the given item
# keep in mind that if there is another element linked to the same priority, the other element will be overriden by the given item
priority_queue.enqueue("first_item", 5)
priority_queue.enqueue("second_item", 5)
# doing this will link priority 5 to str object "second_item" and "first_item" will be ignored

priority_queue.peek() # returns element with minimum or maximum priority in the queue, but doesn't remove it from the queue
# if priority_queue.is_reversed() is False, it returns the element with the maximum priority
# if priority_queue.is_reversed() is True, it returns the element with the minimum priority
# returns None if the queue is empty

priority_queue.dequeue() # same as priority_queue.peek(), but removes the returned element from the queue
# raises a ValueError if the queue is empty 

priority_queue.get(priority) # returns the element linked to the given priority
# returns None if no element is linked to this priority
# raises a TypeError if type(priority) is not int

# the implementation includes an iterator too
for item in priority_queue:
    print(item)
# keep in mind that the iterator uses priority_queue.dequeue() to get the next element, hence after the iteration 
# is finished the priority_queue will be empty
priority_queue.is_empty() # will return True
```

<br> <br>

- **_Graph_** <br>
The graph's implementation is generic: you can specify the type of elements in the graph in the constructor. 
If not specified, it is set to None, hence objects of all types can be added to the graph. You can also set the
directed, oriented and weighted arguments in the constructor if you want to have a graph with a special feature.
By default, those arguments are set to False. Keep in mind that you cannot initialize a graph, which is oriented and
not directed at the same time. <br>
Nodes of the graph are stored in a list and a set, which allows fast checking
whether the graph contains a certain node in cost of memory. The graph doesn't support duplicate node values <br>
Edges of the graph are stored in a square matrix: 2-dimensional list which is resized automatically when needed. 
The initial length of the edges list is 5. A value of None in the matrix represents the absence of an edge. If the graph
is not weighted a value of 1 represents the presence of a node. If the graph is weighted, an edge would be represented by 
its weight in the matrix and it must be either float or int. <br>
The indices in the 2-dimensional list are the indices of the nodes in the list. E.g. <br> 
if the list of nodes is:
```python
nodes = [5.5, "word", 100]
```
and we have a non-directed and non-weighted graph with an edge between 5.5 and 100, the edges matrix will be
```python
edges = [
[None, None, 1, None, None],
[None, None, None, None, None],
[1, None, None, None, None],
[None, None, None, None, None],
[None, None, None, None, None]
]
```
Note the initial size of the matrix, which is 5 by 5 matrix. The indices of 5.5 and 100 in the list of nodes are 0 and 2
respectively and the graph is not directed. That's why edges[0][2] = edges[2][0] = 1.

_API_ :
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structure

graph = Graph() # initialize a graph with None elements type, hence all types of elements can be added to the graph
# the initialized graph is also nor directed, neither oriented, neither weighted

graph = Graph(elements_type=int, directed=True, oriented=False, weighted=True)
# only integers can be added to the initialized graph; the graph is directed, but not oriented; the graph is also weighted
 
graph = Graph(elements_type=str, directed=False, oriented=True, weighted=True)
# this raises a ValueError since a graph cannot be oriented and not directed at the same time

graph = Graph(float, True, True, True)
# only floats can be added to the initialized graph; the graph is directed, oriented and weighted

graph.size() # returns the number of elements in the graph
len(graph) # same as graph.size()
graph.is_empty() # returns True if there are no nodes in the graph and False otherwise

str(graph) # returns a string in the format 'Graph: directed - boolean, oriented - boolean, weighted - boolean'

graph.type() # returns the type of node values in the graph, returns None if all types of elements are allowed
# if this method doesn't return None, only nodes of the returned type can be added to the graph

graph.is_directed() # returns True if the graph is directed and False otherwise

graph.is_oriented() # returns True if the graph is oriented and False otherwise

graph.is_weighted() # returns True if the graph is weighted and False otherwise

item = "test_element"
graph.contains(item) # returns True if item is in the set of nodes of the graph and False otherwise
# raises a TypeError if the type of the graph is not None and is different than the type of the argument
boolean = item in graph # same as graph.contains(item)

first_item = "first_test_item"
second_item = "second_test_item"
graph.contains_edge(first_item, second_item) # returns True if an edge from first_item to second_item exists
# raises a TypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a KeyError if first_item or second_item is not a node that the graph contains
# if the graph is not directed the result will be the same even if you reverse the order of the arguments

graph.get_edge_weight(first_item, second_item)
# raises a TypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a KeyError if first_item or second_item is not a node that the graph contains
# raises a ValueError if the graph is not weighted
# raises a ValueError if an edge between first_item and second_item doesn't exist
# if the graph is not directed the result will be the same even if you reverse the order of the arguments

graph.nodes() # returns a deep copy of the list of nodes of the graph
# a deep copy is returned to avoid manual changes of the graph by changing the elements in the returned list
 
graph.add_node(item) # adds item to the nodes of the graph if it is not already added
# raises a TypeError if the type of the graph is not None and is different than the type of the argument
# raises an AttributeError if item is None
# if item is already added as a node to the graph, the function does nothing

graph.remove_node(item) 
# raises a TypeError if the type of the graph is not None and is different than the type of the argument
# raises a KeyError if item is not a node in the graph
# remove a node in the graph also removes all edges related to this node (going to and from this node)

old_node = "test_old_node"
new_node = "test_new_node"
graph.replace_node(old_node, new_node) # replaces old_node with new_node in the graph list of nodes if possible
# raises a TypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a KeyError if old_node is not a node the graph contains
# raises a KeyError if new_node is a node the graph contains, since duplicate nodes are not allowed

# the replacing of a node in the graph doesn't affect the edges in the graph, e.g.
connected_nodes = graph.edges_of(old_node)
graph.replace_node(old_node, new_node)
new_connected_nodes = graph.edges_of(new_node)
print(connected_nodes == new_connected_nodes) 
# will print True, since edges of the old node are not affected, only the value is replaced
# the method is useful, since it retains the edges of the old node 
# and is faster than first removing the old node and then adding the new node


graph.edges() # returns a deep copy of the square matrix (2D list) representing the edges of the graph
# a deep copy is returned to avoid manual changes of the graph by changing the elements in the returned list

graph.edges_of(item) # returns a list of all nodes to which there is an edge from the argument
# returns an empty list if there are no such nodes
# raises a TypeError if the type of the graph is not None and is different than the type of the argument
# raises a KeyError if the item if not a node in the graph

edge_weight = "test_edge_weight"
graph.add_edge(first_item, second_item, edge_weight) # adds an edge from first_item to second_item with the given edge_weight if appropriate
# edge_weight should only be specified if the graph is weighted, otherwise, just skip this argument (set to None by default)
# raises a TypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a TypeError if edge_weight is specified and is not of type float or int
# raises a KeyError if first_item or second_item is not a node that the graph contains
# raises a ValueError if the graph is weighted and edge_weight is not specified or it is None
# raises a KeyError if the graph is oriented and an edgre from second_item to first_item already exists

graph.remove_edge(first_item, second_item) # removes the edge from first_item to second_item
# if the graph is not directed, this function removes the edge from second_item to first_item too
# raises a TypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a KeyError if first_item or second_item is not a node that the graph contains
# raises a KeyError if there is no edge from first_item to second_item

# the implementation includes an iterator too
for node in graph:
    print(node)
# the iterator goes through all nodes in the graph
# the __iter__ method actually returns the iterator of the list of nodes of the graph
```

<br>

### Algorithms

**_Implementation for sorting algorithms, searching algorithms, n-queen solver algorithm and minimax algorithm 
for playing tic-tac-toe in Python_** <br>

**_Sorting Algorithms in Python - Insertion Sort, Selection Sort, Bubble Sort,
Merge Sort, Quick Sort_** <br>
**All of these are located in the SortingAlgorithms.py module** <br><br>

- **_Insertion Sort_** <br>
Takes a list of elements as an argument and sorts the list. Can be used either with or without
assignment to a variable.<br>

Examples:<br>
```python
from Algorithms.SortingAlgorithms import insertion_sort

elements = [5, 965, -32, 21, 96, -13]

insertion_sort(elements) # sorts the elements argument
print(elements) # prints [-32, -13, 5, 21, 96, 965]

# we can also assign the result like that
elements = insertion_sort(elements)

# or we can assign it to a new variable
new_list = insertion_sort(elements)

# keep in mind the last example creates a new reference to the same list
# that was sorted and it doesn't create a new list
new_list.append(111) # appends 111 to the list that new_list references
print(elements, new_list) # prints the same list twice, because both reference the sorted list
```

- **_Selection Sort_** <br>
Takes a list of elements as an argument and sorts the list. Can be used either with or without
assignment to a variable.<br>

Examples:<br>
```python
from Algorithms.SortingAlgorithms import selection_sort

elements = [5, 965, -32, 21, 96, -13]

selection_sort(elements) # sorts the elements argument
print(elements) # prints [-32, -13, 5, 21, 96, 965]

# we can also assign the result like that
elements = selection_sort(elements)

# or we can assign it to a new variable
new_list = selection_sort(elements)

# keep in mind the last example creates a new reference to the same list
# that was sorted and it doesn't create a new list
new_list.append(111) # appends 111 to the list that new_list references
print(elements, new_list) # prints the same list twice, because both reference the sorted list
```

- **_Bubble Sort_** <br>
Takes a list of elements as an argument and sorts the list. Can be used either with or without
assignment to a variable.<br>

Examples:<br>
```python
from Algorithms.SortingAlgorithms import bubble_sort

elements = [5, 965, -32, 21, 96, -13]

bubble_sort(elements) # sorts the elements argument
print(elements) # prints [-32, -13, 5, 21, 96, 965]

# we can also assign the result like that
elements = bubble_sort(elements)

# or we can assign it to a new variable
new_list = bubble_sort(elements)

# keep in mind the last example creates a new reference to the same list
# that was sorted and it doesn't create a new list
new_list.append(111) # appends 111 to the list that new_list references
print(elements, new_list) # prints the same list twice, because both reference the sorted list
```

- **_Merge Sort_** <br>
Takes a list of elements as an argument and sorts the list. Can only be used with
assignment to a variable. This is because the method returns a new list with the sorted
elements of the argument list.<br>

Examples:<br>
```python
from Algorithms.SortingAlgorithms import merge_sort

elements = [5, 965, -32, 21, 96, -13]

# WRONG WAY - no assignemnt of the result
merge_sort(elements) # CANNOT be used like that
# using this way we ignore the returned new list containing the sorted elements
print(elements) # prints [5, 965, -32, 21, 96, -13]

# RIGHT WAY - assign the result to the same variable
elements = merge_sort(elements) # assign the sorted list to the same variable
print(elements) # prints [-32, -13, 5, 21, 96, 965]

# ANOTHER RIGHT WAY - assign the result to a new variable, thus retain the original list
new_list = merge_sort(elements) # assign the sorted list to a new variable
print(elements) # prints the original list - [5, 965, -32, 21, 96, -13]
print(new_list) # prints the sorted list - [-32, -13, 5, 21, 96, 965]

# different than the last three sorting algorithms, here, the original list is not changed
# and a new list with the sorted elements of the original list is returned
new_list.append(111) # appends 111 only to the sorted new_list
print(elements, new_list) # prints [5, 965, -32, 21, 96, -13], [-32, -13, 5, 21, 96, 965, 111]
```

- **_Quick Sort_** <br>
Takes a list of elements as an argument and sorts the list. Can be used either with or without
assignment to a variable.<br>

Examples:<br>
```python
from Algorithms.SortingAlgorithms import quick_sort

elements = [5, 965, -32, 21, 96, -13]

quick_sort(elements) # sorts the elements argument
print(elements) # prints [-32, -13, 5, 21, 96, 965]

# we can also assign the result like that
elements = quick_sort(elements)

# or we can assign it to a new variable
new_list = quick_sort(elements)

# keep in mind the last example creates a new reference to the same list
# that was sorted and it doesn't create a new list
new_list.append(111) # appends 111 to the list that new_list references
print(elements, new_list) # prints the same list twice, because both reference the sorted list
```

**_Searching Algorithms in Python - Breadth First Search, Depth First Search_** <br>
**All of these are located in the SearchingAlgorithms.py module** <br><br>

- **_Breadth First Search algorithm_** <br>
Implemented in three different functions.<br>

First function - <b>breadth_first_search</b> - takes a graph, a function object and a start
node as arguments. The graph is traversed using the BFS algorithm and for each node the function object passed as argument 
is applied. If the function returns any result (different than None), the result is returned and the traversal is stopped.
The start node argument is optional. If you pass it as None (default option), then the first node in the list of nodes in 
the graph will be used.<br>

The second function - <b>breadth_first_search_list</b> - takes a graph and a start node as arguments. The graph is traversed
using the BFS algorithm and a list of nodes is returned. The order in the list is the same as the nodes traversal order.
Same principles as for the previous function applied here for the start node argument.<br>

The third function - <b>breadth_first_search_generator</b> - absolutely the same idea as breadth_first_search_list. Same arguments,
same implementation, the only difference is that it returns a generator, which yields the nodes from the breath first
search traversal one by one.<br>

Examples of <b>breadth_first_search</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import breadth_first_search # import the bfs function

graph = Graph(int, directed=True) # initialize the graph
for node in range(10):
    graph.add_node(node) # fill the graph with some nodes
# fill the graph with some edges
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(8, 9)

# define a test function to use, keep in mind that the first argument of the function must be the current node 
# that is being traversed
def print_func(current_node):
    print(current_node)

# apply breadth first search with the function defined above
breadth_first_search(graph, print_func, start_node=None)
# the start node is set to None (default option) for clarity reasons
# calling the above function will print the nodes in the following order 0, 1, 3, 4, 2, 6, 5, 7, 8, 9 (BFS traversal)
# each node will be on new line, since each print is a different call to the test_func

# define another test function, but this times a function with arguments, still the first argument must be the current node
# that is being traversed
def search_func(current_node, search_node, nodes_list):
    nodes_list.append(current_node)
    
    if current_node == search_node:
        return True

# apply breadth first search with the function defined above
test_list = []
result = breadth_first_search(graph, search_func, None, 9, test_list)
# NB! when using a function which takes arguments in the bfs method, we must first declare the start_node (set it to None
# if you want to start from the first node in the list of nodes in the graph) and then declare all other arguments that 
# would be passed to the function argument

# calling the function above we want to pass the values 9 and test_list to the search_func function,
# hence we want to search for the value of 9 and append all nodes we traverse to the empty test_list
# if we find the node we are searching for, the function returns True and the traversal stops

# Therefore when the above function is executed, result will be True and test_list would be [0, 1, 3, 4, 2, 6, 5, 7, 8, 9]
# Since 9 is the last node in the bfs traversal, every node would be appended to test_list

# However, if we start the traversal from node 9 and search for node 9 again:
test_list = [] # reset the test_list
result = breadth_first_search(graph, search_func, 9, 9, test_list) # call breadth_first_search
# result would still be True since we find the node 9, but test list would be [9]
# this is because we start from node 9 and we are searching for node 9, hence only the first node is traversed

# Keep in mind that the traversal of the graph will stop only if the function provided in the arguments returns a result
# different than None; if it does - this result is returned and the traversal is stopped

# Another thing to keep in mind is that if we start with a node that is not connected to any nodes, the function will
# traverse only this node
breadth_first_search(graph, print_func, 9) 
# will print only 9, since the graph is directed and there is no edge starting from 9

# Also if we traverse the whole graph and no result is returned, the function will return None
test_list = [] # reset the test_list
result = breadth_first_search(graph, search_func, 9, 100, test_list) # starting from node 9 and searching for node 100
# result would be None and test_list would be [9], as we explained above only node 9 will be traversed

# Errors that might be raised when using breadth_first_search function:
    # TypeError if the first argument is not of type Graph
    # TypeError if the second argument is not callable
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

Examples of <b>breadth_first_search_list</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import breadth_first_search_list # import the bfs function

graph = Graph(elements_type=None, directed=True, oriented=True) # initialize the graph
for node in ["str", 5, 1.5, "float", "int"]:
    graph.add_node(node) # add some nodes in the graph
        
# add some edges in the graph
graph.add_edge("str", 5)
graph.add_edge(5, "int")
graph.add_edge(5, "float")
graph.add_edge("float", 1.5)

# apply the breadth_first_search_list function to the graph
nodes = breadth_first_search_list(graph, start_node=None) # returns the list of nodes in the order of the bfs traversal
# the start node is set to None (default option) for clarity reasons
# after execution, nodes would be ["str", 5, "float", "int", 1.5]

# apply the breadth_first_search_list function to the graph starting from node "float"
nodes = breadth_first_search_list(graph, start_node="float")
# after execution nodes would be ["float", 1.5]

# Errors that might be raised when using breadth_first_search_list function:
    # TypeError if the first argument is not of type Graph
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

Examples of <b>breadth_first_search_generator</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import breadth_first_search_generator # import the bfs function

graph = Graph(elements_type=None, directed=True, oriented=True) # initialize the graph
for node in ["str", 5, 1.5, "float", "int"]:
    graph.add_node(node) # add some nodes in the graph
        
# add some edges in the graph
graph.add_edge("str", 5)
graph.add_edge(5, "int")
graph.add_edge(5, "float")
graph.add_edge("float", 1.5)

# apply the breadth_first_search_generator function to the graph
generator = breadth_first_search_generator(graph, start_node=None) # returns a generator of nodes in the order of the bfs traversal
# the start node is set to None (default option) for clarity reasons
while True:
    try:
        print(next(generator)) # prints the traversed node that was yielded
    except StopIteration as err:
        break
# prints the nodes in the following order: "str", 5, "float", "int", 1.5

# apply the breadth_first_search_generator function to the graph starting from node "float"
nodes = list(breadth_first_search_generator(graph, start_node="float"))
# after execution nodes would be ["float", 1.5]

# Errors that might be raised when using breadth_first_search_generator function:
    # TypeError if the first argument is not of type Graph
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

- **_Depth First Search algorithm_** <br>
Implemented in three different functions.<br>

First function - <b>depth_first_search</b> - takes a graph, a function object and a start
node as arguments. The graph is traversed using the DFS algorithm and for each node the function object passed as argument 
is applied. If the function returns any result (different than None), the result is returned and the traversal is stopped.
The start node argument is optional. If you pass it as None (default option), then the first node in the list of nodes in 
the graph will be used.<br>

The second function - <b>depth_first_search_list</b> - takes a graph and a start node as arguments. The graph is traversed
using the DFS algorithm and a list of nodes is returned. The order in the list is the same as the nodes traversal order.
Same principles as for the previous function applied here for the start node argument.<br>

The third function - <b>depth_first_search_generator</b> - absolutely the same idea as depth_first_search_list. Same arguments,
same implementation, the only difference is that it returns a generator, which yields the nodes from the depth first
search traversal one by one.<br>

Examples of <b>depth_first_search</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import depth_first_search # import the dfs function

graph = Graph(int, directed=True) # initialize the graph
for node in range(10):
    graph.add_node(node) # fill the graph with some nodes
# fill the graph with some edges
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(8, 9)

# define a test function to use, keep in mind that the first argument of the function must be the current node 
# that is being traversed
def print_func(current_node):
    print(current_node)

# apply depth first search with the function defined above
depth_first_search(graph, print_func, start_node=None)
# the start node is set to None (default option) for clarity reasons
# calling the above function will print the nodes in the following order 0, 1, 2, 5, 7, 8, 9, 3, 4, 6 (DFS traversal)
# each node will be on new line, since each print is a different call to the test_func

# define another test function, but this times a function with arguments, still the first argument must be the current node
# that is being traversed
def search_func(current_node, search_node, nodes_list):
    nodes_list.append(current_node)
    
    if current_node == search_node:
        return True

# apply depth first search with the function defined above
test_list = []
result = depth_first_search(graph, search_func, None, 9, test_list)
# NB! when using a function which takes arguments in the dfs method, we must first declare the start_node (set it to None
# if you want to start from the first node in the list of nodes in the graph) and then declare all other arguments that 
# would be passed to the function argument

# calling the function above we want to pass the values 9 and test_list to the search_func function,
# hence we want to search for the value of 9 and append all nodes we traverse to the empty test_list
# if we find the node we are searching for, the function returns True and the traversal stops

# Therefore when the above function is executed, result will be True and test_list would be [0, 1, 2, 5, 7, 8, 9]
# Since 9 is not the last node in the dfs traversal, not every node would be appended to test_list

# However, if we start the traversal from node 9 and search for node 9 again:
test_list = [] # reset the test_list
result = depth_first_search(graph, search_func, 9, 9, test_list) # call depth_first_search
# result would still be True since we find the node 9, but test list would be [9]
# this is because we start from node 9 and we are searching for node 9, hence only the first node is traversed

# Keep in mind that the traversal of the graph will stop only if the function provided in the arguments returns a result
# different than None; if it does - this result is returned and the traversal is stopped

# Another thing to keep in mind is that if we start with a node that is not connected to any nodes, the function will
# traverse only this node
depth_first_search(graph, print_func, 9) 
# will print only 9, since the graph is directed and there is no edge starting from 9

# Also if we traverse the whole graph and no result is returned, the function will return None
test_list = [] # reset the test_list
result = depth_first_search(graph, search_func, 9, 100, test_list) # starting from node 9 and searching for node 100
# result would be None and test_list would be [9], as we explained above only node 9 will be traversed

# Errors that might be raised when using depth_first_search function:
    # TypeError if the first argument is not of type Graph
    # TypeError if the second argument is not callable
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

Examples of <b>depth_first_search_list</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import depth_first_search_list # import the dfs function

graph = Graph(elements_type=None, directed=True, oriented=True) # initialize the graph
for node in ["str", 5, 1.5, "float", "int"]:
    graph.add_node(node) # add some nodes in the graph
        
# add some edges in the graph
graph.add_edge("str", 5)
graph.add_edge(5, "int")
graph.add_edge(5, "float")
graph.add_edge("float", 1.5)

# apply the depth_first_search_list function to the graph
nodes = depth_first_search_list(graph, start_node=None) # returns the list of nodes in the order of the dfs traversal
# the start node is set to None (default option) for clarity reasons
# after execution, nodes would be ["str", 5, "float", 1.5, "int"]

# apply the depth_first_search_list function to the graph starting from node "float"
nodes = depth_first_search_list(graph, start_node="float")
# after execution nodes would be ["float", 1.5]

# Errors that might be raised when using depth_first_search_list function:
    # TypeError if the first argument is not of type Graph
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

Examples of <b>depth_first_search_generator</b> function:<br>
```python
from ADTs.AbstractDataStructures import Graph # import the graph data structures
from Algorithms.SearchAlgorithms import depth_first_search_generator # import the dfs function

graph = Graph(elements_type=None, directed=True, oriented=True) # initialize the graph
for node in ["str", 5, 1.5, "float", "int"]:
    graph.add_node(node) # add some nodes in the graph
        
# add some edges in the graph
graph.add_edge("str", 5)
graph.add_edge(5, "int")
graph.add_edge(5, "float")
graph.add_edge("float", 1.5)

# apply the depth_first_search_generator function to the graph
generator = depth_first_search_generator(graph, start_node=None) # returns a generator of nodes in the order of the dfs traversal
# the start node is set to None (default option) for clarity reasons
while True:
    try:
        print(next(generator)) # prints the traversed node that was yielded
    except StopIteration as err:
        break
# prints the nodes in the following order: "str", 5, "float", 1.5, "int"

# apply the depth_first_search_generator function to the graph starting from node "float"
nodes = list(depth_first_search_generator(graph, start_node="float"))
# after execution nodes would be ["float", 1.5]

# Errors that might be raised when using depth_first_search_generator function:
    # TypeError if the first argument is not of type Graph
    # ValueError if the graph is empty - I mean with no nodes in it
    # TypeError if start_node is provided and its type is different than the type of the graph 
        # (of course, this applies only if graph.type() is not None)
    # KeyError if start_node is not a node, which the graph contains
```

<br>

**_Backtracking algorithm for the famous N-queen problem_** <br>
**This is located in the N-queen.py module** <br>

Examples:<br>
```python
from Algorithms.nQueen import n_queen
# returns the solution indices of the places to put a queen
n_queen(4) # returns [1, 3, 0, 2]
# this means (0th row, 1st column), (1st row, 3rd column), (2nd row, 0th column) and
# (3rd row, 2nd column) are the places to put a queen on the 4x4 board

# if you want to save all the states that were covered before finding a solution, pass a second argument as empty list
covered_paths = []
n_queen(6, covered_paths)
# after execution covered_paths will be a list of lists, and every list in it would be a state the algorithm has covered
```

<br>

**_Minimax algorithm for the tic-tac-toe game. It returns the best move to
make in a tic-tac-toe game and the result that this move will lead to : 10 for a win,
 -10 for a loss and 0 for a tie._** <br>
**This is located in the minimax.py module** <br>

Examples:<br>
```python
from Algorithms.minimax import minimax

# you need to give a 2D array representing the board of the game as an argument
board = []
board.append([1,0,-1])
board.append([0,0,1])
board.append([1,0,-1])
# 1 -> player calling minimax tick,
# -1 -> opposite player tick
# 0 -> no player has ticked this place

# calling minimax we get a tuple (score, position)
# position is a tuple representing a position in the 2D array (i,j)
# score is 10 -> for a move leading to a win,
# -10 -> for a move leading to a loss, 0 -> for a move leading to a tie

minimax(board) # returns (10, (1, 0))

# this means that by putting 1 into position (1,0) you will get a win
```

<br>

### Basic applications of data structures and algorithms

**_Expression Evaluator_** <br>
**This is located in ExpressionEvaluator.py** <br><br>

The ExpressionEvaluator.py file contains an implementation of a simple
algorithm to evaluate simple mathematical expressions. By simple I mean including
only operations such as addition, subtraction, multiplication, division.
The result is returned as a float number.<br>

Examples:<br>
```python
from Applications.ExpressionEvaluator import evaluate_expression

expression = "(7 - 4)*(5 + 3)/2" # the expression is given as a string
print(evaluate_expression(expression)) # prints 12.0

# CANNOT evaluate an empty string
print(evaluate_expression("")) # raises a ValueError

# CAN evaluate a single operand, returns the operand
print(evaluate_expression("5")) # prints 5.0

# CANNOT evaluate single operator
print(evaluate_expression("+")) # raises a ValueError
print(evaluate_expression("-")) # raises a ValueError
print(evaluate_expression("*")) # raises a ValueError
print(evaluate_expression("/")) # raises a ValueError

# CAN evaluate valid expressions for which the parenthesis ordering is valid too
print(evaluate_expression("1 - 32*0.5 + 12")) # prints -3.0
print(evaluate_expression("6/3 - 2*3 + 1 - 5/2 + 3/8 + 0.125")) # prints -5.0
print(evaluate_expression("2+3-4/2*2+3*2/0.5")) # prints 16.0
```

<br>

**_Tic-Tac-Toe game_** <br>
**This is located in TicTacToe.py** <br><br>

The TicTacToe.py file contains a simple tic-tac-toe game where you play
against the computer. The computer plays by using the minimax algorithm in
minimax.py. When you finish a game click Enter to start a new game where you
go first or click Space to start a new game where the computer goes first.<br>

Examples:<br>
```python
# just run the TicTacToe.py file and the game will start.
```

**_N-Queen Visualization_** <br>
**This is located in nQueenVisualization.py** <br><br>

The nQueenVisualization.py file contains a simple pygame script, which shows how will the queens will be placed on a 
square grid when applying the algorithm.<br>

Examples:<br>
```python
# just run the nQueenVisualization.py file and the window will open
# When running you have to pass as a command line argument the number of queens you want to place on the board

# e.g. in command prompt type: python nQueenVisualization.py 6

# keep in mind that the minimum number of queens for which there is a solution is 4, hence this is the default option
# if an argument is not passed
```

**_N-Queen Animation_** <br>
**This is located in nQueenAnimation.py** <br><br>

The nQueenAnimation.py file contains a simple pygame animation, which shows the process of searching for a solution using
the bactracking algorithm for the n-queen problem.<br>

Examples:<br>
```python
# just run the nQueenAnimation.py file and the animation will start
# When running you have to pass as a command line argument the number of queens you want to place on the board

# e.g. in command prompt type: python nQueenAnimation.py 6

# keep in mind that the minimum number of queens for which there is a solution is 4, hence this is the default option
# if an argument is not passed

# another thing to keep in mind is that the speed of the animation may be increased or decreased by changing the delay
# in the pygame.time.delay method (line 117 - nQueenAnimation.py)
```