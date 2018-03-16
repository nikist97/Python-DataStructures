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
