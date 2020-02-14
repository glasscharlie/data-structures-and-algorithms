import collections

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
    
    def breadth_first(self, node):
        visited = set()
        q = collections.deque()
        q.appendleft(node)
        while q:
            current = q.pop()
            visited.add(current)
            lst = self.get_neighbors(current)
            if lst:
                for nodes in lst:
                    if isinstance(nodes, node) and nodes not in visited:
                        q.appendleft(vert)


