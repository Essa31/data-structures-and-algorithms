import pytest
from graph_depth_first.graph_depth_first import *

g = Graph()

g.addEdge("A", "D")
g.addEdge("A", "B")

g.addEdge("B", "A")
g.addEdge("B", "D")
g.addEdge("B", "C")

g.addEdge("C", "B")
g.addEdge("C", "G")

g.addEdge("G", "C")

g.addEdge("D", "A")
g.addEdge("D", "B")
g.addEdge("D", "F")
g.addEdge("D", "H")
g.addEdge("D", "E")

g.addEdge("E", "D")

g.addEdge("H", "D")
g.addEdge("H", "F")

g.addEdge("F", "D")
g.addEdge("F", "H")




def test1():
    assert =="A, D, B, C, G, F, H, E,"