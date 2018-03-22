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
