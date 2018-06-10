# Abstract and Tree-like Data Structures - Python

**_The repository contains Python-based implementations for some of the most famous data structures._**

### Installation:
Please use 'pip install pythonic-data-structures'.

### Issues:
Please register any issues you find in the github repository so that they can be fixed as soon as possible.

### Requirements:
There are no dependencies on external libraries. However, a Python 3.x version is required.

### Docs:
_Navigate to data structures:_ [Stack](#stack), [Queue](#queue), [Min Binary Heap](#minbh), 
[Max Binary Heap](#maxbh), [Priority Queue](#pq), [Duplicate Priority Queue](#dpq), [Graph](#graph)
<br><br>


### Data Structures

**_Implementation for Stack, Queue, Max Binary Heap, Min Binary Heap, Priority Queue and Graph in Python_** <br>
**These are located in the AbstractDataStructures.py and TreeDataStructures.py modules** <br><br>

- **_Stack<a name="stack"></a> (First-In-Last-Out)_** <br>
The Stack's implementation wraps around the python deque object, but is also generic: you can specify the type of elements 
in the stack in the constructor. If not specified, it is set to None and elements of any type can be added to the stack. The
implementation includes all the common operations of a stack: peek, push, pop, size, etc.<br>

_API_ :
```python
from DataStructures.AbstractDataStructures import Stack # import the stack data structure

stack = Stack() # type is set to None, items of any types can be added
stack = Stack(elements_type = int) # type is set to int, hence only integers can be pushed

stack.size() # returns the number of elements in the stack
len(stack) # same as stack.size()
stack.is_empty() # returns True if stack is empty and False otherwise

str(stack) # returns the string representation of the python deque object containing the elements of the stack

item = "test_item"
stack.contains(item) # returns True if the item is in the stack and False otherwise
# contains raises a StackTypeError if the type of the stack is not None and is different than the type of the parameter
boolean = item in stack 
# same as boolean = stack.contains(item)

stack.type() # returns the type of the elements in the stack, None if no type is specified

stack.peek() # returns the last element that was added to the stack, but doesn't remove it
# peek returns None if there are no elements in the stack

stack.pop() # same as peek(), but removes the last element that was added to the stack
# pop raises an EmptyStackError if there are no elements in the stack

element = "test_item"
stack.push(element) # pushes the element to the top of the stack
# push raises a StackTypeError if the stack has a specified type for elements and the argument is not of that type

# the implementation includes an iterator
for element in stack:
    print(element)
# keep in mind that the iterator uses stack.pop() to get the next element, hence
# after the iteration is over the stack would be empty

stack.remove(element) # removes the element from the stack
# raises a StackTypeError if the stack has a specified type for elements and the argument is not of that type
# raises a StackElementError if the stack doesn't contain the element specified as argument
```

<br> <br>

- **_Queue<a name="queue"></a> (First-In-First-Out)_** <br>
The Queue's implementation wraps around the python deque object, but is also generic: you can specify the type of elements in the queue in the constructor.
If not specified, it is set to None and elements of any type can be added to the queue. The
implementation includes all the common operations of a queue: enqueue, dequeue, peek, size, etc.<br>

_API_ :
```python
from DataStructures.AbstractDataStructures import Queue # import the queue data structure
queue = Queue() # type is set to None, items of any types can be added
queue = Queue(elements_type = str) # type is set to str, hence only strings can be enqueued

queue.size() # returns the number of elements in the queue
len(queue) # same as queue.size()
queue.is_empty() # return True if queue is empty and False otherwise

str(queue) # returns the string representation of the python deque object containing the elements of the queue

item = "test_item"
queue.contains(item) # returns True if the item is in the queue and False otherwise
# contains raises a QueueTypeError if the type of the queue is not None and is different 
# than the type of the parameter
boolean = item in queue 
# same as boolean = queue.contains(item)

queue.type() # returns the type of the elements in the queue, None if no type is specified

queue.peek() # returns the first element that was added to the queue, but doesn't remove it
# peek returns None if there are no elements in the queue

queue.dequeue() # same as peek(), but removes the first element that was added to the queue
# dequeue raises a EmptyQueueError if there are no elements in the queue

element = "test_element"
queue.enqueue(element) # enqueues the element to the back of the queue
# enqueue raises a QueueTypeError if the queue has a specified type for elements
# and the argument is not of that type

# the implementation includes an iterator
for element in queue:
    print(element)
# keep in mind that the iterator uses queue.dequeue() to get the next element, hence
# after the iteration is over the queue would be empty

queue.remove(element) # removes the element from the queue
# raises a QueueTypeError if the queue has a specified type for elements and the argument is not of that type
# raises a QueueElementError if the queue doesn't contain the element specified as argument
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

MinBinaryHeap<a name="minbh"></a> _API_ : 
```python
from DataStructures.AbstractDataStructures import MinBinaryHeap # import the min heap

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
# add raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap

min_heap.peek_min() # returns the minimum element (the root), but doesn't remove it from the heap
# returns None if heap is empty

min_heap.remove_min() # returns the minimum element (the root) and removes it from the heap
# the method replaces the root with the second minimum element in the heap
# it raises a EmptyBinaryHeapError if the heap is empty

# returns the minimum element (the root) and removes it from the heap, by replacing it with the element argument
min_heap.replace_root(element) 
# same as min_heap.remove_min() followed by min_heap.add(element), but replace_root() is faster
# raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a EmptyBinaryHeapError if the heap is empty

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
        print(next(heap_iter))
    except StopIteration:
        break
min_heap.size() # will return 0 after iteration is finished, as explained above

old_element, new_element = 10, 100
min_heap.replace(old_element, new_element) # replaces the old element with the new element and readjusts the heap after
# the replacement
# raises a BinaryHeapTypeError if the type of the first or the second argument is not the same as the type of the 
# elements in the heap
# raises a BinaryHeapElementError if the old_element argument is not contained in the heap
# raises a EmptyBinaryHeapError if the heap is empty

min_heap.remove(element)  # removes the element and readjusts the heap after deletion
# raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a BinaryHeapElementError if the element argument is not contained in the heap
# raises a EmptyBinaryHeapError if the heap is empty
```

<br>

MaxBinaryHeap<a name="maxbh"></a> _API_:
```python
from DataStructures.AbstractDataStructures import MaxBinaryHeap # import the max heap

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
# add raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap

max_heap.peek_max() # returns the maximum element (the root), but doesn't remove it from the heap
# returns None if heap is empty

max_heap.remove_max() # returns the maximum element (the root) and removes it from the heap
# the method replaces the root with the second maximum element in the heap
# it raises a EmptyBinaryHeapError if the heap is empty

# returns the maximum element (the root) and removes it from the heap, by replacing it with the element argument
max_heap.replace_root(element) 
# same as max_heap.remove_max() followed by max_heap.add(element), but replace_root() is faster
# raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a EmptyBinaryHeapError if the heap is empty

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
        print(next(heap_iter))
    except StopIteration:
        break
max_heap.size() # will return 0 after iteration is finished, as explained above

old_element, new_element = 10, 100
max_heap.replace(old_element, new_element) # replaces the old element with the new element and readjusts the heap after
# the replacement
# raises a BinaryHeapTypeError if the type of the first or the second argument is not the same as the type of the 
# elements in the heap
# raises a BinaryHeapElementError if the old_element argument is not contained in the heap
# raises a EmptyBinaryHeapError if the heap is empty

max_heap.remove(element)  # removes the element and readjusts the heap after deletion
# raises a BinaryHeapTypeError if the type of the argument is not the same as the type of the elements in the heap
# raises a BinaryHeapElementError if the element argument is not contained in the heap
# raises a EmptyBinaryHeapError if the heap is empty
```


<br> <br>

- **_Priority Queue<a name="pq"></a>_** <br>
The Priority Queue's implementation is generic: you can specify the type of elements in the queue in the constructor. 
If not specified, it is set to None, hence objects of all types can be added to the priority queue. You can also set the reverse
argument in the constructor. If reverse is set to False (default) the queue dequeues the element with the greatest priority, 
else if the reverse argument is set to True - it dequeues the element with the lowest priority. The implementation includes 
all the common operations of a priority queue: enqueue, dequeue, peek, size, etc.<br>

_API_ :
```python
from DataStructures.AbstractDataStructures import PriorityQueue # import the priority queue data structure

priority_queue = PriorityQueue() # type is set to default None, hence objects of all types can be enqueued to the queue
# the reverse argument is set to default False, hence dequeue returns the element with the highest priority

priority_queue = PriorityQueue(elements_type=str, reverse=True) # type is set to str, hence only strings can be enqueued
# the reverse argument is set to True, hence dequeue returns the element with the lowest priority

priority_queue.size() # returns the number of elements in the queue
len(priority_queue) # same as priority_queue.size()
priority_queue.is_empty() # returns True if there are no elements in the queue and False otherwise


str(priority_queue) # returns a string of the dictionary linking priorities with elements in the queue

priority_queue.type() # returns the type of elements that can be enqueued in the priority queue
# if this method returns None, objects of all types can be enqueued

priority_queue.is_reversed() # returns True if the queue dequeues the element with the lowest priority
# returns False if the queue dequeues the element with the highest priority

priority = 10
priority_queue.contains_priority(priority) # returns True if the queue has an element, linked to the given priority and False otherwise
# contains raises a PriorityQueueTypeError if type of priority is not int

element = "test_element"
priority_queue.contains_element(element) # returns True if an element is contained in the queue
# raises PriorityQueueTypeError if priority_queue.type() is not None and is different than the type of the given element
boolean = element in priority_queue # same as priority_queue.contains_element(priority)

item = "test_item"
priority_queue.enqueue(item, priority) # enqueues the given item and links it the given priority
# raises PriorityQueueTypeError if type(priority) is not int
# raises PriorityQueueTypeError if priority_queue.type() is not None and is different than the type of the given item
# keep in mind that if there is another element linked to the same priority, the old element will be replaced
# by the new element
priority_queue.enqueue("first_item", 5)
priority_queue.enqueue("second_item", 5)
# doing this will link priority 5 to str object "second_item" while str object "first_item" will be ignored and 
# removed from the queue
# Another thing to note is that you can enqueue the same element to different priorities
priority_queue.enqueue("item", 10)
priority_queue.enqueue("item", 11)

priority_queue.peek() # returns element with minimum or maximum priority in the queue, but doesn't remove it from the queue
# if priority_queue.is_reversed() is False, it returns the element with the maximum priority
# if priority_queue.is_reversed() is True, it returns the element with the minimum priority
# returns None if the queue is empty

priority_queue.dequeue() # same as priority_queue.peek(), but removes the returned element from the queue
# raises a EmptyPriorityQueueError if the queue is empty 

priority_queue.get(priority) # returns the element linked to the given priority
# returns None if no element is linked to this priority
# raises a PriorityQueueTypeError if type(priority) is not int

# the implementation includes an iterator too
for item in priority_queue:
    print(item)
# keep in mind that the iterator uses priority_queue.dequeue() to get the next element, hence after the iteration 
# is finished the priority_queue will be empty
priority_queue.is_empty() # will return True

priority_queue.replace_priority(element, priority) # replaces the given element's priority with the new priority argument
# returns a boolean representing whether the element's priority has been replaced
# raises PriorityQueueTypeError if type(priority) is not int
# raises PriorityQueueTypeError if priority_queue.type() is not None and is different than the type of the given element
# raises PriorityQueueElementError if the element is not contained in the queue
# if there is another element already assigned to the new priority, the old element will be replaced with the element 
# given as argument, thus the old element will be ignored and removed

# you can also pass a third argument to the replace_priority method - comparison
comparison_type = 1
priority_queue.replace_priority(element, priority, comparison=comparison_type)
# returns a boolean representing whether the element's priority has been replaced
# by doing so the priority of the element will only be replaced if a certain type of comparison between 
# the two priorities holds
# if comparison is 1, the priorities will be replaced if the new priority is greater than the old priority
# if comparison is -1, the priorities will be replaced if the new priority is less than the old priority
# if comparison is None (default), the priorities will always be replaced
# raises ValueError if comparison is not -1, 1 or None

priority_queue.remove_element(element) # finds and removes the element from the queue
# raises PriorityQueueTypeError if priority_queue.type() is not None and is different than the type of the given element
# raises PriorityQueueElementError if the queue doesn't contain the element
```

<br> <br>

- **_Duplicate Priority Queue<a name="dpq"></a>_** <br>
The Duplicate Priority Queue behaves exactly as the normal Priority Queue with the only difference being that it allows
elements with duplicated priorities. This, however is not true for the normal Priority Queue, since in its implementation
if you enqueue an element with a priority that is already linked to some old element, then the old element would be replaced
by the new enqueued element. By using a duplicate priority queue, no elements are ignored. Instead, if you dequeue and there 
are two elements with the same priority, then they will be dequeued in the order they were enqueued.<br>

_API_ :
```python
from DataStructures.AbstractDataStructures import DuplicatePriorityQueue # import the priority queue data structure

queue = DuplicatePriorityQueue() # type is set to default None, hence objects of all types can be enqueued to the queue
# the reverse argument is set to default False, hence dequeue returns the element with the highest priority

queue = DuplicatePriorityQueue(elements_type=str, reverse=True) # type is set to str, hence only strings can be enqueued
# the reverse argument is set to True, hence dequeue returns the element with the lowest priority

queue.size() # returns the number of elements in the queue, 
# elements with the same priority are NOT counted as one element, but as ordinary elements
len(queue) # same as queue.size()
queue.is_empty() # returns True if there are no elements in the queue and False otherwise


str(queue) # returns a string of the dictionary linking priorities with elements in the queue
# keep in mind that if there is a priority linked to more than one element, the string representation will return
# the priority linked to a Queue object

queue.type() # returns the type of elements that can be enqueued in the priority queue
# if this method returns None, objects of all types can be enqueued

queue.is_reversed() # returns True if the queue dequeues the element with the lowest priority
# returns False if the queue dequeues the element with the highest priority

priority = 10
queue.contains_priority(priority) # returns True if the queue has an element or elements, linked to the given priority and False otherwise
# contains raises a PriorityQueueTypeError if type of priority is not int

element = "test_element"
queue.contains_element(element) # returns True if an element is contained in the queue
# raises PriorityQueueTypeError if queue.type() is not None and is different than the type of the given element
boolean = element in queue # same as queue.contains_element(priority)

item = "test_item"
queue.enqueue(item, priority) # enqueues the given item and links it the given priority
# raises PriorityQueueTypeError if type(priority) is not int
# raises PriorityQueueTypeError if priority_queue.type() is not None and is different than the type of the given item
# in this implementation of a priority queue, if there is already an item with the given priority in the queue, then both 
# items will be retained and when dequeueing they will be dequeued in the order they were enqueued
queue.enqueue("first_item", 5)
queue.enqueue("second_item", 5)
queue.dequeue() # dequeues "first_item"
queue.dequeue() # dequeues "second_item"
# Another thing to note is that you can enqueue the same element to different priorities
queue.enqueue("item", 10)
queue.enqueue("item", 11)

queue.peek() # returns element with minimum or maximum priority in the queue, but doesn't remove it from the queue
# if priority_queue.is_reversed() is False, it returns the element with the maximum priority
# if priority_queue.is_reversed() is True, it returns the element with the minimum priority
# returns None if the queue is empty
# if there are more than one elements with the same priority, peek() will return the first element that was enqueued

queue.dequeue() # same as priority_queue.peek(), but removes the returned element from the queue
# raises a EmptyPriorityQueueError if the queue is empty 
# if there are more than one elements with the same priority, dequeue() will return and remove them in the order they were
# enqueued

queue.get(priority) # returns the element linked to the given priority
# returns None if no element is linked to this priority
# raises a PriorityQueueTypeError if type(priority) is not int
# if there are more than one elements with the same priority, get() will return the first element that was enqueued

# the implementation includes an iterator too
for item in queue:
    print(item)
# keep in mind that the iterator uses priority_queue.dequeue() to get the next element, hence after the iteration 
# is finished the queue will be empty
queue.is_empty() # will return True

queue.replace_priority(element, priority) # replaces the given element's priority with the new priority argument
# raises PriorityQueueTypeError if type(priority) is not int
# raises PriorityQueueTypeError if queue.type() is not None and is different than the type of the given element
# raises PriorityQueueElementError if the element is not contained in the queue
# in this implementation duplicated priorities are allowed, hence no elements will be ignored even if there is already
# an element assigned to the new priority

# you can also pass a third argument to the replace_priority method - comparison
comparison_type = 1
queue.replace_priority(element, priority, comparison=comparison_type)
# by doing so the priority of the element will only be replaced if a certain type of comparison between 
# the two priorities holds
# if comparison is 1, the priorities will be replaced if the new priority is greater than the old priority
# if comparison is -1, the priorities will be replaced if the new priority is less than the old priority
# if comparison is None (default), the priorities will always be replaced
# raises ValueError if comparison is not -1, 1 or None

queue.remove_element(element) # finds and removes the element from the queue
# raises PriorityQueueTypeError if queue.type() is not None and is different than the type of the given element
# raises PriorityQueueElementError if the queue doesn't contain the element
```

<br> <br>

- **_Graph<a name="graph"></a>_** <br>
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
from DataStructures.AbstractDataStructures import Graph # import the graph data structure

graph = Graph() # initialize a graph with None elements type, hence all types of elements can be added to the graph
# the initialized graph is also neither directed, nor oriented, nor weighted

graph = Graph(elements_type=int, directed=True, oriented=False, weighted=True)
# only integers can be added to the initialized graph; the graph is directed, but not oriented; the graph is also weighted
 
graph = Graph(elements_type=str, directed=False, oriented=True, weighted=True)
# this raises an InvalidGraphError since a graph cannot be oriented and not directed at the same time

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
# raises a GraphTypeError if the type of the graph is not None and is different than the type of the argument
boolean = item in graph # same as graph.contains(item)

first_item = "first_test_item"
second_item = "second_test_item"
graph.contains_edge(first_item, second_item) # returns True if an edge from first_item to second_item exists
# raises a GraphTypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a GraphElementError if first_item or second_item is not a node that the graph contains
# if the graph is not directed the result will be the same even if you reverse the order of the arguments

graph.get_edge_weight(first_item, second_item)
# raises a GraphTypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a GraphElementError if first_item or second_item is not a node that the graph contains
# raises a GraphEdgeError if the graph is not weighted
# raises a GraphEdgeError if an edge between first_item and second_item doesn't exist
# if the graph is not directed the result will be the same even if you reverse the order of the arguments

graph.nodes() # returns a deep copy of the list of nodes of the graph
# a deep copy is returned to avoid manual changes of the graph by changing the elements in the returned list
 
graph.add_node(item) # adds item to the nodes of the graph if it is not already added
# raises a GraphTypeError if the type of the graph is not None and is different than the type of the argument
# raises an GraphElementError if item is None
# if item is already added as a node to the graph, the function does nothing

graph.remove_node(item) 
# raises a GraphTypeError if the type of the graph is not None and is different than the type of the argument
# raises a GraphElementError if item is not a node in the graph
# remove a node in the graph also removes all edges related to this node (going to and from this node)

old_node = "test_old_node"
new_node = "test_new_node"
graph.replace_node(old_node, new_node) # replaces old_node with new_node in the graph list of nodes if possible
# raises a GraphTypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a GraphElementError if old_node is not a node the graph contains
# raises a GraphElementError if new_node is a node the graph contains, since duplicate nodes are not allowed

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
# raises a GraphTypeError if the type of the graph is not None and is different than the type of the argument
# raises a GraphElementError if the item if not a node in the graph

edge_weight = "test_edge_weight"
graph.add_edge(first_item, second_item, edge_weight) # adds an edge from first_item to second_item with the given edge_weight if appropriate
# edge_weight should only be specified if the graph is weighted, otherwise, just skip this argument (set to None by default)
# raises a GraphTypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a GraphTypeError if edge_weight is specified and is not of type float or int
# raises a GraphElementError if first_item or second_item is not a node that the graph contains
# raises a GraphEdgeError if the graph is weighted and edge_weight is not specified or it is None
# raises a GraphEdgeError if the graph is oriented and an edge from second_item to first_item already exists

graph.remove_edge(first_item, second_item) # removes the edge from first_item to second_item
# if the graph is not directed, this function removes the edge from second_item to first_item too
# raises a GraphTypeError if the type of the graph is not None and is different than the type of any of the arguments
# raises a GraphElementError if first_item or second_item is not a node that the graph contains
# raises a GraphEdgeError if there is no edge from first_item to second_item

# the implementation includes an iterator too
for node in graph:
    print(node)
# the iterator goes through all nodes in the graph
# the __iter__ method actually returns the iterator of the list of nodes of the graph
```