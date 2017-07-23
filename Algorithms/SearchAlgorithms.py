"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from ADTs.AbstractDataStructures import Stack, Queue, Graph


# Breadth-First-Search (BFS) algorithm for graph traversing
# takes a function as argument and applies the function to every node
# if the result of the function is different than None, it returns the result
def breadth_first_search(graph, func, start_node=None, *args, **kwargs):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if not callable(func):
        raise TypeError("The second argument of this function must be a function.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    queue = Queue(graph.type())

    if start_node is None:
        for node in graph:
            queue.enqueue(node)
            break
    else:
        queue.enqueue(start_node)

    explored = set()

    while not queue.is_empty():
        node = queue.dequeue()
        explored.add(node)

        result = func(node, *args, **kwargs)
        if result is not None:
            return result

        for edge_node in graph.edges_of(node):
            if edge_node not in explored and edge_node not in queue:
                queue.enqueue(edge_node)


# Breadth-First-Search (BFS) algorithm for graph traversing
# it returns a list of nodes of the graph in the order they would be traversed using BFS
def breadth_first_search_list(graph, start_node=None):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    queue = Queue(graph.type())

    if start_node is None:
        for node in graph:
            queue.enqueue(node)
            break
    else:
        queue.enqueue(start_node)

    explored = set()
    result_nodes = []

    while not queue.is_empty():
        node = queue.dequeue()
        explored.add(node)
        result_nodes.append(node)

        for edge_node in graph.edges_of(node):
            if edge_node not in explored and edge_node not in queue:
                queue.enqueue(edge_node)

    return result_nodes


# Breadth-First-Search (BFS) algorithm for graph traversing
# a generator function, which yields the nodes of the graph in the order of the bfs traversal
def breadth_first_search_generator(graph, start_node=None):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    queue = Queue(graph.type())

    if start_node is None:
        for node in graph:
            queue.enqueue(node)
            break
    else:
        queue.enqueue(start_node)

    explored = set()

    while not queue.is_empty():
        node = queue.dequeue()
        explored.add(node)
        yield node

        for edge_node in graph.edges_of(node):
            if edge_node not in explored and edge_node not in queue:
                queue.enqueue(edge_node)


# Depth-First-Search (DFS) algorithm for graph traversing
# takes a function as argument and applies the function to every node
# if the result of the function is different than None, it returns the result
def depth_first_search(graph, func, start_node=None, *args, **kwargs):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if not callable(func):
        raise TypeError("The second argument of this function must be a function.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    stack = Stack(graph.type())

    if start_node is None:
        for node in graph:
            stack.push(node)
            break
    else:
        stack.push(start_node)

    explored = set()

    while not stack.is_empty():
        node = stack.pop()
        explored.add(node)

        result = func(node, *args, **kwargs)
        if result is not None:
            return result

        for edge_node in graph.edges_of(node)[:: -1]:
            if edge_node not in explored and edge_node not in stack:
                stack.push(edge_node)


# Depth-First-Search (DFS) algorithm for graph traversing
# it returns a list of nodes of the graph in the order they would be traversed using DFS
def depth_first_search_list(graph, start_node=None):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    stack = Stack(graph.type())

    if start_node is None:
        for node in graph:
            stack.push(node)
            break
    else:
        stack.push(start_node)

    explored = set()
    result_nodes = []

    while not stack.is_empty():
        node = stack.pop()
        explored.add(node)
        result_nodes.append(node)

        for edge_node in graph.edges_of(node)[:: -1]:
            if edge_node not in explored and edge_node not in stack:
                stack.push(edge_node)

    return result_nodes


# Depth-First-Search (DFS) algorithm for graph traversing
# a generator function, which yields the nodes of the graph in the order of the dfs traversal
def depth_first_search_generator(graph, start_node=None):
    if type(graph) != Graph:
        raise TypeError("The first argument of this function must be of type Graph.")

    if graph.is_empty():
        raise ValueError("You cannot traverse an empty graph")

    try:
        if start_node is not None and start_node not in graph:
            raise KeyError("The starting node argument must be a node from the graph argument.")
    except TypeError as err:
        raise err

    stack = Stack(graph.type())

    if start_node is None:
        for node in graph:
            stack.push(node)
            break
    else:
        stack.push(start_node)

    explored = set()

    while not stack.is_empty():
        node = stack.pop()
        explored.add(node)
        yield node

        for edge_node in graph.edges_of(node)[:: -1]:
            if edge_node not in explored and edge_node not in stack:
                stack.push(edge_node)
