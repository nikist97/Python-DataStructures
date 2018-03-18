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
    is not found in the it.
    """

    def __init__(self, msg):
        super().__init__(msg)


class BinaryHeapTypeError(TypeError):
    """
    A custom type of error, when a binary heap operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)
