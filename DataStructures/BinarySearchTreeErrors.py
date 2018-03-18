class BinarySearchTreeElementError(KeyError):
    """
    A custom type of error, when an operation is performed, which requires an element from the binary search tree, but this element
    is not found in it.
    """

    def __init__(self, msg):
        super().__init__(msg)


class BinarySearchTreeTypeError(TypeError):
    """
    A custom type of error, when a binary search tree operation is performed with arguments of the wrong type.
    """

    def __init__(self, msg):
        super().__init__(msg)
