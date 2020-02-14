from graph import Graph, Node
import pytest

def test_add_node():
    graph = Graph()
    expected = 'apple' 
    actual = graph.add_node('apple').value
    assert actual == expected

def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node('apple')
    expected = 1
    actual = graph.size()
    assert actual == expected


def test_add_edge_interloper_start():
    graph = Graph()
    start = Node('start')
    end = graph.add_node('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)




def test_add_edge_interloper_end():
    graph = Graph()
    end = Node('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_groovy():
    graph = Graph()
    end = graph.add_node('end')
    start = graph.add_node('start')
    graph.add_edge(start, end)

def test_add_edge_effect():
    graph = Graph()
    end = graph.add_node('pear')
    start = graph.add_node('peach')
    graph.add_edge(start, end)
    expected = (end, 0)
    actual = graph._adjacency_list[start][0]
    assert actual == expected

def test_add_edge_effect_with_weight():
    graph = Graph()
    end = graph.add_node('pear')
    start = graph.add_node('peach')
    graph.add_edge(start, end, 44)
    expected = (end, 44)
    actual = graph._adjacency_list[start][0]
    assert actual == expected


def test_get_nodes():
    graph = Graph()
    graph.add_node('pear')
    graph.add_node('peach')
    Node('loner')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected


def test_get_neighbors():
    graph = Graph()
    pear = graph.add_node('pear')
    peach = graph.add_node('peach')
    graph.add_edge(peach, pear, 44)
    neighbors = graph.get_neighbors(peach)
    assert len(neighbors) == 1
    assert neighbors[0][0].value == 'pear'
    assert isinstance(neighbors[0][0], Node)
    assert neighbors[0][1] == 44



def test_breadth_first():
    graph = Graph()

    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add all edges
    graph.add_edge(apple, banana, 1)

    graph.add_edge(banana, apple, 2)
    graph.add_edge(banana, cantelope, 3)
    graph.add_edge(banana, figs, 4)

    graph.add_edge(cantelope, banana, 5)
    graph.add_edge(cantelope, figs, 6)
    graph.add_edge(cantelope, dates, 7)

    graph.add_edge(figs, banana, 8)
    graph.add_edge(figs, cantelope, 9)
    graph.add_edge(figs, dates, 10)
    graph.add_edge(figs, eggplant, 20)

    graph.add_edge(dates, cantelope, 30)
    graph.add_edge(dates, figs, 40)
    graph.add_edge(dates, eggplant, 50)

    graph.add_edge(eggplant, figs, 60)
    graph.add_edge(eggplant, dates, 70)

