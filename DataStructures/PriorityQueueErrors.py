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
