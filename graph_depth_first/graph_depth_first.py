class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])

    def depth_first(self, node=None):
        if node is None:
            return []
        result = []

        stack = []
        start = node
        visited_node = set()

        stack.append(start)
        visited_node.add(start)

        while len(stack):
            current = stack.pop()

            result.append(current.value)

            neighbors = self.get_neighbors(current)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited_node:
                    stack.append(neighbor)
                    visited_node.add(neighbor)

        return result



