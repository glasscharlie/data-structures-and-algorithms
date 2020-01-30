class Node:
    def __init__(self, value):
        self.value = value

class Graph:

    def __init__(self):
        self._adjacency_list = {}


    def add_node(self, value):
        n = Node(value)
        self._adjacency_list[n] = []
        return n


    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_node, end_node, weight=0):
        if start_node not in self._adjacency_list:
            raise KeyError('Start Node not in Graph')
        if end_node not in self._adjacency_list:
            raise KeyError('End Node not in Graph')
        adjacencies = self._adjacency_list[start_node]
        adjacencies.append((end_node,weight))


    def get_nodes(self):
        return self._adjacency_list.keys()


    def get_neighbors(self, node):
        return self._adjacency_list[node]

def get_edge(graph, lst):
    includes = True
    price = 0
    for i in range(0, len(lst) - 1):
        neighbors = graph.get_neighbors(lst[i])
        for j in range(0, len(neighbors)):
            if (neighbors[j][0].value) == (lst[i + 1].value):
                price += neighbors[j][1]
                includes = True
                break
            else: 
                includes = False
        if includes == False:
            return {False, '$0'}

    return {True: f'${price}'}

g = Graph()
Pandora = g.add_node('Pandora')
Arandelle = g.add_node('Arandelle')
Metro = g.add_node('Metro')
Monster = g.add_node('Monster')
Naboo = g.add_node('Naboo')
Narnia = g.add_node('Narnia')
g.add_edge(Pandora, Metro, 82)
g.add_edge(Pandora, Arandelle, 150)
g.add_edge(Monster, Metro, 105)
g.add_edge(Metro, Naboo,  26)
g.add_edge(Narnia, Naboo,  250)
g.add_edge(Narnia, Metro, 37)
g.add_edge(Arandelle, Metro,  99)
g.add_edge(Arandelle, Monster,  42)
g.add_edge(Naboo, Monster,  73)
print(get_edge(g,[Pandora, Metro, Naboo]))