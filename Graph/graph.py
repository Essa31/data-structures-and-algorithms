class Vertex:
    """
    The nodes within the graph
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    """
    The connection between to nodes within the graph
    """
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:
    """
    Graph data structure object
    """
    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        """
        Arguments: value
        Add a node to the graph
        Returns: The added node
        """
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex is None:
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)

    def get_nodes(self):
        """
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        return self.__adj_list.keys()

    def size(self):
        """
        Arguments: node
        Returns a collection of edges connected to the given node
        """
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        """
        Arguments: none
        Returns the total number of nodes in the graph
        """
        return self.__adj_list.get(ver, [])