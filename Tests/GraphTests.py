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

# Simple unittests for the graph data structure
import unittest

from ADTs.AbstractDataStructures import Graph


class GraphTest(unittest.TestCase):

    def test_size(self):
        graph = Graph(int, True)
        self.assertEqual(graph.size(), 0, "Wrong size at initialization")
        self.assertEqual(len(graph), 0, "Wrong size at initialization")

        for i in range(5):
            graph.add_node(i**2)
        self.assertTrue(len(graph), graph.size())
        self.assertEqual(graph.size(), 5, "Wrong size after multiple addition of nodes")

        graph.remove_node(4)
        graph.remove_node(16)
        self.assertEqual(len(graph), 3, "Wrong size after removing nodes")

        graph.add_edge(1, 9)
        graph.add_edge(9, 1)
        self.assertEqual(graph.size(), 3, "Wrong size after adding edges")

        graph.remove_node(9)
        self.assertEqual(len(graph), 2, "Wrong size after removing a node with edges")

        graph = Graph()
        self.assertEqual(len(graph), 0, "Wrong size at initialization")

        graph.add_node("item")
        graph.add_node(120)
        graph.add_node(2.5)
        self.assertEqual(graph.size(), 3, "Wrong size after addition of multiple nodes")

        graph.add_edge("item", 120)
        self.assertEqual(graph.size(), 3, "Wrong size after adding an edge")

        graph.remove_node(2.5)
        self.assertEqual(len(graph), 2, "Wrong size after removing a node")

    def test_str(self):
        graph = Graph()
        self.assertEqual(str(graph), "Graph: directed - False, oriented - False, weighted - False",
                         "Wrong string implementation")

        graph = Graph(None, True, False, False)
        self.assertEqual(str(graph), "Graph: directed - True, oriented - False, weighted - False",
                         "Wrong string implementation")

        graph = Graph(str, True, True, False)
        self.assertEqual(str(graph), "Graph: directed - True, oriented - True, weighted - False",
                         "Wrong string implementation")

        graph = Graph(int, True, True, True)
        self.assertEqual(str(graph), "Graph: directed - True, oriented - True, weighted - True",
                         "Wrong string implementation")

        graph = Graph(int, False, False, True)
        self.assertEqual(str(graph), "Graph: directed - False, oriented - False, weighted - True",
                         "Wrong string implementation")

        with self.assertRaises(ValueError):
            Graph(int, False, True, True)

        with self.assertRaises(ValueError):
            Graph(str, False, True, False)

    def test_type(self):
        graph = Graph()
        self.assertEqual(graph.type(), None, "Wrong type at initialization")

        graph = Graph(directed=True, oriented=False, weighted=False)
        self.assertEqual(graph.type(), None, "Wrong type at initialization")

        graph.add_node(0)
        graph.add_node(5.25)
        graph.add_node("string")
        graph.add_edge("string", 0)

        graph = Graph(str)
        self.assertEqual(graph.type(), str, "Wrong type at initialization")

        graph.add_node("string")
        with self.assertRaises(TypeError):
            graph.add_node(3)
        graph.add_node("another string")
        graph.add_edge("string", "another string")
        with self.assertRaises(TypeError):
            graph.add_edge(2, 3)

    def test_contains(self):
        graph = Graph()

        graph.add_node(5)
        graph.add_node("str")
        graph.add_node(5.7)
        graph.add_node(7)
        self.assertTrue("str" in graph, "Wrong implementation of contains")
        self.assertTrue(graph.contains("str"), "Wrong implementation of contains")
        self.assertTrue(7 in graph, "Wrong implementation of contains")

        graph.add_edge(5, 5.7)
        self.assertTrue(graph.contains(5), "Wrong implementation of contains after adding an edge")

        graph.remove_node("str")
        self.assertFalse("str" in graph, "Wrong implementation of contains after removing a node")

        graph = Graph(int)
        with self.assertRaises(TypeError):
            graph.contains("str")
        with self.assertRaises(TypeError):
            graph.contains(5.5)
        graph.add_node(3)
        graph.add_node(1)
        self.assertTrue(1 in graph)
        self.assertTrue(graph.contains(3))
        graph.remove_node(3)
        graph.remove_node(1)
        for i in range(10):
            self.assertFalse(graph.contains(i), "Wrong implementation of contains after removing all nodes")

    def test_contains_edge(self):
        graph = Graph()

        with self.assertRaises(KeyError):
            graph.contains_edge(1, 2)

        graph.add_node(1)
        graph.add_node(11.1)
        graph.add_node(str(1))
        graph.add_node(True)

        graph.add_edge(1, 11.1)
        graph.add_edge(True, 1)
        graph.add_edge(1, 1)

        with self.assertRaises(KeyError):
            graph.contains_edge(0, 5)

        self.assertTrue(graph.contains_edge(1, 1), "Wrong implementation of contains_edge")
        self.assertTrue(graph.contains_edge(True, 1), "Wrong implementation of contains_edge")
        self.assertTrue(graph.contains_edge(11.1, 1), "Wrong implementation of contains_edge")

        graph.remove_edge(1, True)
        self.assertFalse(graph.contains_edge(True, 1), "Wrong implementation of contains_edge")
        graph.remove_node(1)
        with self.assertRaises(KeyError):
            self.assertFalse(graph.contains_edge(1, 1))

        graph = Graph(str, True)
        graph.add_node("string")
        graph.add_node("word")
        graph.add_node("sentence")
        graph.add_edge("string", "sentence")
        self.assertTrue(graph.contains_edge("string", "sentence"), "Wrong implementation of contains_edge")
        self.assertFalse(graph.contains_edge("sentence", "string"), "Wrong implementation of contains_edge")

        with self.assertRaises(TypeError):
            graph.contains_edge(2, 3)

        with self.assertRaises(KeyError):
            graph.contains_edge("a", "b")

        graph.remove_edge("string", "sentence")
        self.assertFalse(graph.contains_edge("string", "sentence"), "Wrong implementation of contains_edge")

    def test_edges_of(self):
        graph = Graph(int)

        with self.assertRaises(KeyError):
            graph.edges_of(5)

        for i in range(10):
            graph.add_node(i)

        with self.assertRaises(TypeError):
            graph.edges_of(str(5))

        graph.add_edge(1, 3)
        graph.add_edge(7, 9)
        graph.add_edge(9, 0)
        graph.add_edge(3, 5)
        graph.add_edge(3, 9)
        nodes = graph.edges_of(3)
        nodes.sort()
        self.assertEqual(nodes, [1, 5, 9], "Wrong implementation of edges_of")
        nodes = graph.edges_of(9)
        nodes.sort()
        self.assertEqual(nodes, [0, 3, 7], "Wrong implementation of edges_of")

        graph = Graph(None, True, True, False)
        nodes = ["str", 1, 10.5, "float", False, True]
        for node in nodes:
            graph.add_node(node)

        with self.assertRaises(KeyError):
            graph.edges_of(10)

        graph.add_edge(True, "float")
        graph.add_edge("str", True)
        graph.add_edge(True, False)
        graph.add_edge(True, 1)
        self.assertEqual(graph.edges_of(True), [1, 'float', False], "Wrong implementation of edges_of")

        graph = Graph(str)

        with self.assertRaises(TypeError):
            graph.edges_of(10)

        with self.assertRaises(KeyError):
            graph.edges_of("")

        graph.add_node("word")
        graph.add_node("str")
        graph.add_edge("word", "str")
        graph.add_edge("word", "word")
        self.assertEqual(graph.edges_of("word"), ["word", "str"])
        self.assertEqual(graph.edges_of("str"), ["word"])

    def test_edge_weight(self):
        graph = Graph(weighted=True)
        nodes = ["string", 1, 2, 3, 4.5, "num"]
        for node in nodes:
            graph.add_node(node)

        with self.assertRaises(ValueError):
            graph.add_edge(1, 2)

        with self.assertRaises(TypeError):
            graph.add_edge(1, 2, "str")

        graph.add_edge(1, 2, 10.0)
        self.assertEqual(graph.get_edge_weight(1, 2), 10.0, "Wrong get_edge_weight implementation")
        graph.add_edge(1, 2, 5)
        self.assertEqual(graph.get_edge_weight(1, 2), 5, "Wrong get_edge_weight implementation")

        graph = Graph(int, directed=True, weighted=True)
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(1, 2, 3)
        graph.add_edge(3, 4, 7)
        graph.add_edge(4, 3, 7.5)
        graph.add_edge(1, 4, 5)
        self.assertEqual(graph.get_edge_weight(1, 4), 5, "Wrong get_edge_weight implementation")
        with self.assertRaises(ValueError):
            graph.get_edge_weight(2, 1)
        self.assertEqual(graph.get_edge_weight(3, 4), 7, "Wrong get_edge_weight implementation")
        self.assertEqual(graph.get_edge_weight(4, 3), 7.5, "Wrong get_edge_weight implementation")

        graph = Graph(float, True, True, True)
        for i in range(10, 15, 1):
            graph.add_node(i/10)
        graph.add_edge(1.1, 1.2, 2.3)
        graph.add_edge(1.2, 1.4, 2.6)
        self.assertEqual(graph.get_edge_weight(1.2, 1.4), 2.6, "Wrong get_edge_weight implementation")
        with self.assertRaises(ValueError):
            graph.get_edge_weight(1.4, 1.2)

    def test_add_edge(self):
        graph = Graph()
        for node in [1, 1.1, "1", True]:
            graph.add_node(node)

        with self.assertRaises(KeyError):
            graph.add_edge(11, True)

        with self.assertRaises(KeyError):
            graph.add_edge(True, False)

        graph.add_edge(1, "1")
        graph.add_edge(1, 1)

        self.assertTrue(graph.contains_edge("1", 1), "Wrong add_edge implementation")
        self.assertTrue(graph.contains_edge(1, 1), "Wrong add_edge implementation")
        self.assertEqual(graph.edges_of(1), [1, "1"], "Wrong add_edge implementation")

        graph = Graph(int, True, True, True)

        with self.assertRaises(TypeError):
            graph.add_edge("string", 0)

        with self.assertRaises(TypeError):
            graph.add_edge(0, "string")

        for i in range(10):
            graph.add_node(i)

        with self.assertRaises(KeyError):
            graph.add_edge(11, 0)

        with self.assertRaises(ValueError):
            graph.add_edge(5, 6)

        with self.assertRaises(TypeError):
            graph.add_edge(5, 6, "weight")

        graph.add_edge(5, 6, 25.5)
        self.assertTrue(graph.contains_edge(5, 6), "Wrong add_edge implementation")
        self.assertFalse(graph.contains_edge(6, 5), "Wrong add_edge implementation")
        self.assertEqual(graph.get_edge_weight(5, 6), 25.5, "Wrong add_edge implementation")

        graph.add_edge(5, 9, -10)
        self.assertEqual(graph.get_edge_weight(5, 9), -10, "Wrong add_edge implementation")
        with self.assertRaises(ValueError):
            graph.get_edge_weight(9, 5)
        self.assertEqual(graph.edges_of(5), [6, 9], "Wrong add_edge implementation")
        self.assertEqual(graph.edges_of(3), [], "Wrong add_edge implementation")

        with self.assertRaises(KeyError):
            graph.add_edge(9, 5, 10)

    def test_remove_edge(self):
        graph = Graph()
        with self.assertRaises(KeyError):
            graph.remove_edge(1, 9)

        for node in [1, 1.1, "1", False]:
            graph.add_node(node)

        graph.add_edge(1, 1.1)
        graph.add_edge("1", False)

        with self.assertRaises(KeyError):
            graph.add_edge(5, 5)

        self.assertTrue(graph.contains_edge(1, 1.1))
        graph.remove_edge(1.1, 1)
        self.assertFalse(graph.contains_edge(1.1, 1),  "Wrong remove_edge implementation")
        self.assertEqual(graph.edges_of(1), [], "Wrong remove_edge implementation")

        graph = Graph(float, directed=True, oriented=True)
        for node in range(0, 101, 1):
            graph.add_node(node/3)

        with self.assertRaises(TypeError):
            graph.remove_edge(1, 2)
        with self.assertRaises(KeyError):
            graph.remove_edge(105.2, 205.2)
        with self.assertRaises(KeyError):
            graph.remove_edge(10.0, 20.0)

        graph.add_edge(10.0, 20.0)
        graph.add_edge(20.0, 30.0)

        self.assertTrue(graph.contains_edge(20.0, 30.0))
        graph.remove_edge(20.0, 30.0)
        self.assertFalse(graph.contains_edge(20.0, 30.0), "Wrong remove_edge implementation")

        self.assertEqual(graph.edges_of(20.0), [], "Wrong remove_edge implementation")

        self.assertEqual(len(graph.edges()), 160, "Wrong remove_edge implementation")

    def test_edges(self):
        graph = Graph(int, directed=True)
        for node in range(5):
            graph.add_node(node)
        edges = graph.edges()
        for l in edges:
            self.assertEqual(l, [None]*5, "Wrong edges implementation")

        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        edges = graph.edges()
        self.assertEqual(edges[0][1], 1, "Wrong edges implementation")
        self.assertEqual(edges[1][0], None, "Wrong edges implementation")
        self.assertEqual(edges[2][1], None, "Wrong edges implementation")
        self.assertEqual(edges[1][2], 1, "Wrong edges implementation")
        edges.append([])
        self.assertNotEqual(graph.edges(), edges, "Wrong edges implementation")

    def test_add_node(self):
        with self.assertRaises(TypeError):
            Graph(5)

        graph = Graph()
        with self.assertRaises(AttributeError):
            graph.add_node(None)
        self.assertTrue(graph.is_empty())
        graph.add_node(1)
        graph.add_node(5.5)
        graph.add_node("string")
        self.assertEqual(len(graph), 3, "Wrong add_node implementation")
        self.assertEqual(graph.nodes(), [1, 5.5, "string"], "Wrong add_node implementation")

        graph = Graph(int)
        with self.assertRaises(TypeError):
            graph.add_node(5.0)
        self.assertEqual(len(graph.edges()), 5, "Wrong number of edges at initialization")
        for i in range(100):
            graph.add_node(i*2)
        self.assertEqual(len(graph.edges()), 160, "Wrong add_node implementation")
        graph.add_node(2)
        self.assertEqual(len(graph), 100, "Wrong add_node implementation")
        graph.add_node(1)
        self.assertEqual(len(graph), 101, "Wrong add_node implementation")
        graph.remove_node(1)

    def test_remove_node(self):
        graph = Graph()
        with self.assertRaises(KeyError):
            graph.remove_node(0)

        graph.add_node(1)
        graph.add_node(1.1)
        graph.add_node("1")
        self.assertEqual(graph.size(), 3)
        self.assertTrue(1 in graph)
        with self.assertRaises(KeyError):
            graph.remove_node("1.1")

        graph.remove_node(1)
        self.assertEqual(len(graph), 2, "Wrong remove_node implementation")
        self.assertFalse(1 in graph, "Wrong remove_node implementation")

        graph = Graph(str)
        with self.assertRaises(TypeError):
            graph.remove_node(4)
        with self.assertRaises(KeyError):
            graph.remove_node("")

        for i in range(50):
            graph.add_node(str(i))
            self.assertTrue(str(i) in graph)
        for j in range(25):
            graph.remove_node(str(j))
            self.assertFalse(str(j) in graph, "Wrong remove_node implementation")

        self.assertEqual(len(graph), 25)

    def test_nodes(self):
        graph = Graph()
        self.assertEqual(graph.nodes(), [], "Wrong nodes at initialization")
        ints = list(range(250, 275))
        for i in ints:
            graph.add_node(i)
        floats = [k/10 for k in range(25, 50)]
        for j in floats:
            graph.add_node(j)

        original_list = ints + floats
        original_list.sort()
        nodes = graph.nodes()
        nodes.sort()
        self.assertEqual(nodes, original_list, "Wrong nodes implementation")

        nodes.append(10)
        self.assertNotEqual(nodes, original_list, "Wrong nodes implementation")
        nodes = graph.nodes()
        nodes.sort()
        self.assertEqual(nodes, original_list, "Wrong nodes implementation")

        graph.add_node(10000)
        original_list.append(10000)
        nodes = graph.nodes()
        nodes.sort()
        self.assertEqual(nodes, original_list, "Wrong nodes implementation")

    def test_iterator(self):
        graph = Graph(float)

        init_list = [x/10 for x in range(10)]
        for node in init_list:
            graph.add_node(node)

        new_list = [node for node in graph]
        new_list.sort()
        self.assertEqual(new_list, init_list, "Wrong iterator implementation")

        graph = Graph(int, True, True, True)
        init_list = [i for i in range(100)]
        for node in init_list:
            graph.add_node(node)
        for j in range(0, 100, 10):
            init_list.remove(j)
            graph.remove_node(j)

        new_list = [k for k in graph]
        new_list.sort()
        self.assertEqual(new_list, init_list, "Wrong iterator implementation")

    def test_replace_node(self):
        graph = Graph(int, directed=False)

        with self.assertRaises(TypeError):
            graph.replace_node("str", 5)

        with self.assertRaises(TypeError):
            graph.replace_node(5, "str")

        for i in range(10):
            graph.add_node(i)

        with self.assertRaises(KeyError):
            graph.replace_node(55, 6)

        with self.assertRaises(KeyError):
            graph.replace_node(5, 5)
        with self.assertRaises(KeyError):
            graph.replace_node(4, 9)

        graph.add_edge(1, 3)
        graph.add_edge(1, 5)
        graph.add_edge(6, 2)
        graph.add_edge(2, 1)

        self.assertEqual(graph.edges_of(1), [2, 3, 5])
        graph.replace_node(1, 11)
        self.assertEqual(graph.edges_of(11), [2, 3, 5], "Wrong replace_node implementation.")
        with self.assertRaises(KeyError):
            graph.edges_of(1)
        with self.assertRaises(KeyError):
            graph.replace_node(1, 2)

        graph.replace_node(9, 99)
        self.assertEqual(graph.edges_of(99), [], "Wrong replace_nood implementation")

        graph = Graph()
        for node in ["string", 5.5, 10, 10.1, "word"]:
            graph.add_node(node)

        with self.assertRaises(KeyError):
            graph.replace_node(5, "5")

        with self.assertRaises(KeyError):
            graph.replace_node(5.5, "word")

        graph.add_edge(5.5, 10)
        graph.add_edge(10.1, 5.5)
        graph.add_edge("string", "word")
        graph.add_edge("word", 5.5)

        self.assertEqual(graph.edges_of(5.5), [10, 10.1, "word"])
        graph.replace_node(5.5, "5.5")
        graph.replace_node(10, "10")
        graph.replace_node(10.1, "10.1")

        for test_node in [5.5, 10, 10.1]:
            self.assertTrue(str(test_node) in graph, "Wrong replace_node implementation")
            self.assertFalse(test_node in graph, "Wrong replce_node implementation")

        self.assertEqual(graph.edges_of("5.5"), ["10", "10.1", "word"], "Wrong replace_node implementation")
        self.assertEqual(graph.edges_of("10"), ["5.5",], "Wrong replace_node implementation")
