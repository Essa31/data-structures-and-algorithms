import pytest
from Graph.graph import *

# test adding node to graph

def test_adding1(graph_empty):
    graph_empty.add_node(10)
    assert graph_empty.size() == 1


#test adding edge to graph

def test_adding2(graph_empty):
    a = graph_empty.add_node(7)
    e = graph_empty.add_node(6)
    graph_empty.add_edge(a, e)
    assert graph_empty.get_neighbors(a)[0].vertex == e


#test getting all nodes within graph

def test_getting1(graph):
    arr_nodes = []

    for i in graph.get_nodes():

        arr_nodes+=[i.value]

    assert arr_nodes == ['A', 'B', 'E', 'C', 'D']


#test getting graph with only one edge and node

def test_getting2(graph_empty):
    b = graph_empty.add_node("A")
    graph_empty.add_edge(b, None)
    assert graph_empty.size() == 1
    assert graph_empty.get_neighbors(b)[0].vertex is None


# test getting all neighbors of node within graph

def test_get_neighbors(graph):
    arr_neighbors = []
    arr_nodes = [i for i in graph.get_nodes()]
    for i in graph.get_neighbors(arr_nodes[0]):

        arr_neighbors+=[i.vertex.value]

    assert arr_neighbors == ['B', 'E', 'C']


#test getting all neighbors of node within graph with their weights

def test_get_neighbors2(graph):
    arr_neighbors=[]
    arr_nodes = [i for i in graph.get_nodes()]

    for i in graph.get_neighbors(arr_nodes[0]):

        arr_neighbors += [[i.vertex.value, i.weight]]

    assert arr_neighbors == [['B', 0], ['E', 0], ['C', 0]]


def test_empty_graph(graph_empty):
    assert graph_empty.size() == 0


@pytest.fixture
def graph_empty():
    graph_empty = Graph()
    return graph_empty


@pytest.fixture
def graph():
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    e = graph.add_node('E')
    c = graph.add_node('C')
    d = graph.add_node('D')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(a, e)
    graph.add_edge(e, a)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(b, e)
    graph.add_edge(e, d)
    graph.add_edge(e, c)

    return graph