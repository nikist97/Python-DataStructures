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

# simple unittests for the depth first search algorithm

import unittest
from Algorithms.SearchAlgorithms import depth_first_search, depth_first_search_list, depth_first_search_generator
from DataStructures.AbstractDataStructures import Graph


class DFSTest(unittest.TestCase):

    def test_dfs(self):

        def test_func(node, nodes_list, search_value):
            nodes_list.append(node)

            if node == search_value:
                return True

        test_list = []

        with self.assertRaises(TypeError):
            depth_first_search(None, test_func, None)

        graph = Graph(int)
        with self.assertRaises(ValueError):
            depth_first_search(graph, test_func, None, test_list)

        with self.assertRaises(TypeError):
            depth_first_search(graph, "string")

        nodes = [node for node in range(10)]
        for node in nodes:
            graph.add_node(node)

        with self.assertRaises(KeyError):
            depth_first_search(graph, test_func, 100)
        with self.assertRaises(TypeError):
            depth_first_search(graph, test_func, "string")

        self.assertEqual(depth_first_search(graph, test_func, None, test_list, "search_value"), None,
                         "Wrong dfs implementation")
        self.assertEqual(test_list, [0], "Wrong dfs implementation")
        test_list = []

        self.assertTrue(depth_first_search(graph, test_func, 5, test_list, 5), "Wrong dfs implementation")
        self.assertEqual(test_list, [5], "Wrong dfs implementation")
        test_list = []

        graph.add_edge(0, 1)
        graph.add_edge(3, 0)
        graph.add_edge(1, 2)
        graph.add_edge(4, 0)
        graph.add_edge(5, 2)
        graph.add_edge(6, 4)
        graph.add_edge(7, 5)
        graph.add_edge(5, 8)
        graph.add_edge(8, 9)

        self.assertTrue(depth_first_search(graph, test_func, None, test_list, 9), "Wrong dfs implementation")
        self.assertEqual(test_list, [0, 1, 2, 5, 7, 8, 9], "Wrong dfs implementation")
        test_list = []

        graph = Graph(elements_type=None, directed=True, oriented=True)
        for node in ["str", 5, 1.5, "float", "int"]:
            graph.add_node(node)

        graph.add_edge("str", 5)
        graph.add_edge(5, "int")
        graph.add_edge(5, "float")
        graph.add_edge("float", 1.5)

        self.assertTrue(depth_first_search(graph, test_func, None, test_list, "int"), "Wrong dfs implementation")
        self.assertEqual(test_list, ["str", 5, "float", 1.5, "int"], "Wrong dfs implementation")
        test_list = []

        self.assertFalse(depth_first_search(graph, test_func, None, [], 3.14), "Wrong dfs implementation")

        self.assertTrue(depth_first_search(graph, test_func, "float", test_list, 1.5), "Wrong dfs implementation")
        self.assertEqual(test_list, ["float", 1.5], "Wrong dfs implementation")

    def test_dfs_list(self):

        graph = Graph(int)

        with self.assertRaises(TypeError):
            depth_first_search_list(None, None)

        with self.assertRaises(ValueError):
            depth_first_search_list(graph, None)

        for node in range(10):
            graph.add_node(node)

        with self.assertRaises(KeyError):
            depth_first_search_list(graph, 11)
        with self.assertRaises(TypeError):
            depth_first_search_list(graph, "string")

        self.assertEqual(depth_first_search_list(graph, None), [0], "Wrong dfs implementation")
        self.assertEqual(depth_first_search_list(graph, 5), [5], "Wrong dfs implementation")

        graph.add_edge(0, 1)
        graph.add_edge(3, 0)
        graph.add_edge(1, 2)
        graph.add_edge(4, 0)
        graph.add_edge(5, 2)
        graph.add_edge(6, 4)
        graph.add_edge(7, 5)
        graph.add_edge(5, 8)
        graph.add_edge(8, 9)

        self.assertEqual(depth_first_search_list(graph), [0, 1, 2, 5, 7, 8, 9, 3, 4, 6], "Wrong dfs implementation")
        self.assertEqual(depth_first_search_list(graph, 9), [9, 8, 5, 2, 1, 0, 3, 4, 6, 7],
                         "Wrong dfs implementation")

        graph = Graph(elements_type=None, directed=True, oriented=True)
        for node in ["str", 5, 1.5, "float", "int"]:
            graph.add_node(node)

        graph.add_edge("str", 5)
        graph.add_edge(5, "int")
        graph.add_edge(5, "float")
        graph.add_edge("float", 1.5)

        self.assertEqual(depth_first_search_list(graph, None), ["str", 5, "float", 1.5, "int"],
                         "Wrong dfs implementation")
        self.assertEqual(depth_first_search_list(graph, "float"), ["float", 1.5], "Wrong dfs implementation")

    def test_dfs_generator(self):

        graph = Graph(int)

        generator = depth_first_search_generator(None, None)
        with self.assertRaises(TypeError):
            next(generator)

        generator = depth_first_search_generator(graph, None)
        with self.assertRaises(ValueError):
            next(generator)

        for node in range(10):
            graph.add_node(node)

        generator = depth_first_search_generator(graph, 11)
        with self.assertRaises(KeyError):
            next(generator)
        generator = depth_first_search_generator(graph, "string")
        with self.assertRaises(TypeError):
            next(generator)

        self.assertEqual([i for i in depth_first_search_generator(graph, None)], [0], "Wrong dfs implementation")
        self.assertEqual([i for i in depth_first_search_generator(graph, 5)], [5], "Wrong dfs implementation")

        graph.add_edge(0, 1)
        graph.add_edge(3, 0)
        graph.add_edge(1, 2)
        graph.add_edge(4, 0)
        graph.add_edge(5, 2)
        graph.add_edge(6, 4)
        graph.add_edge(7, 5)
        graph.add_edge(5, 8)
        graph.add_edge(8, 9)

        self.assertEqual(list(depth_first_search_generator(graph)), [0, 1, 2, 5, 7, 8, 9, 3, 4, 6],
                         "Wrong dfs implementation")
        test_list = []
        for node in depth_first_search_generator(graph, 9):
            test_list.append(node)
        self.assertEqual(test_list, [9, 8, 5, 2, 1, 0, 3, 4, 6, 7],
                         "Wrong dfs implementation")

        graph = Graph(elements_type=None, directed=True, oriented=True)
        for node in ["str", 5, 1.5, "float", "int"]:
            graph.add_node(node)

        graph.add_edge("str", 5)
        graph.add_edge(5, "int")
        graph.add_edge(5, "float")
        graph.add_edge("float", 1.5)

        test_list = []
        generator = depth_first_search_generator(graph, None)
        while True:
            try:
                test_list.append(next(generator))
            except StopIteration:
                break
        self.assertEqual(test_list, ["str", 5, "float", 1.5, "int"],
                         "Wrong dfs implementation")
        self.assertEqual(list(depth_first_search_generator(graph, "float")), ["float", 1.5],
                         "Wrong dfs implementation")
