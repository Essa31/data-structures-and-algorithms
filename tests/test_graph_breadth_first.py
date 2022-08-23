import pytest
from graph_breadth_first.graph_breadth_first import *


def test_breadth_first_traversal_on_one_node(intial_graph):
    Pandora = intial_graph.add_node('Pandora')
    assert intial_graph.breadth_first(Pandora) == ['Pandora']


def test_breadth_first_traversal(intial_graph):
    Pandora = intial_graph.add_node('Pandora')
    Arendelle = intial_graph.add_node('Arendelle')
    Metroville = intial_graph.add_node('Metroville')
    Monstroplolis = intial_graph.add_node('Monstroplolis')
    Narnia = intial_graph.add_node('Narnia')
    Naboo = intial_graph.add_node('Naboo')
    intial_graph.add_edge(Pandora, Arendelle)
    intial_graph.add_edge(Arendelle, Metroville)
    intial_graph.add_edge(Arendelle, Monstroplolis)
    intial_graph.add_edge(Metroville, Arendelle)
    intial_graph.add_edge(Metroville, Monstroplolis)
    intial_graph.add_edge(Metroville, Narnia)
    intial_graph.add_edge(Metroville, Naboo)
    intial_graph.add_edge(Monstroplolis, Arendelle)
    intial_graph.add_edge(Monstroplolis, Metroville)
    intial_graph.add_edge(Monstroplolis, Naboo)
    intial_graph.add_edge(Naboo, Narnia)
    intial_graph.add_edge(Naboo, Metroville)
    intial_graph.add_edge(Naboo, Monstroplolis)
    intial_graph.add_edge(Narnia, Naboo)
    intial_graph.add_edge(Narnia, Metroville)

    actual = intial_graph.breadth_first(Pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

    assert actual == expected


@pytest.fixture
def intial_graph():
    graph = Graph()
    return graph