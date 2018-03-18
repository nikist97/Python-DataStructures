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
