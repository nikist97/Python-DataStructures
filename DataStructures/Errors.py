class EmptyStackError(ValueError):
    """
    A custom type of error, when an operation is performed, which requires a non-empty stack, but an empty stack is
    calling the function.
    """

    def __init__(self, msg):
        super().__init__(msg)


class StackElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the stack, but this element
    is not found in the stack.
    """

    def __init__(self, msg):
        super().__init__(msg)


class StackTypeError(TypeError):
    """
    A custom type of error, when a stack operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)


class EmptyQueueError(ValueError):
    """
    A custom type of error, when an operation is performed, which requires a non-empty queue, but an empty queue is
    calling the function.
    """

    def __init__(self, msg):
        super().__init__(msg)


class QueueElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the queue, but this element
    is not found in the queue.
    """

    def __init__(self, msg):
        super().__init__(msg)


class QueueTypeError(TypeError):
    """
    A custom type of error, when a queue operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)


class EmptyPriorityQueueError(ValueError):
    """
    A custom type of error, when an operation is performed, which requires a non-empty priority queue, but an empty one is
    calling the function.
    """

    def __init__(self, msg):
        super().__init__(msg)


class PriorityQueueElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the priority queue, but this element
    is not found in it.
    """

    def __init__(self, msg):
        super().__init__(msg)


class PriorityQueueTypeError(TypeError):
    """
    A custom type of error, when a priority queue operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)


class InvalidGraphError(ValueError):
    """
    A custom type of error, when an invalid graph is being created, e.g. oriented but not directed
    """

    def __init__(self, msg):
        super().__init__(msg)


class GraphElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the graph, but this element
    is not found in it or there is another error related to the element.
    """

    def __init__(self, msg):
        super().__init__(msg)


class GraphEdgeError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an edge from the graph, but this edge
    is not found in it or there is another error related to the edge.
    """

    def __init__(self, msg):
        super().__init__(msg)


class GraphTypeError(TypeError):
    """
    A custom type of error, when a graph operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)


class EmptyBinaryHeapError(ValueError):
    """
    A custom type of error, when an operation is performed, which requires a non-empty binary heap, but an empty one is
    calling the function.
    """

    def __init__(self, msg):
        super().__init__(msg)


class BinaryHeapElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the binary heap, but this element
    is not found in it.
    """

    def __init__(self, msg):
        super().__init__(msg)


class BinaryHeapTypeError(TypeError):
    """
    A custom type of error, when a binary heap operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)
