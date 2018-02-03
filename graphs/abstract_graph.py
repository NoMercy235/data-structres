import abc


class Graph(abc.ABC):

    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight=0):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

    def vertex_valid(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex %d is incorrect." % v)

    def weight_valid(self, weight):
        if weight < 1:
            raise ValueError("Weight %d incorrect" % weight)