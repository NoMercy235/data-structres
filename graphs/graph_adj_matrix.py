import numpy as np
from graphs.abstract_graph import Graph


class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        self.vertex_valid(v1)
        self.vertex_valid(v2)
        self.weight_valid(weight)

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        self.vertex_valid(v)

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        self.vertex_valid(v)
        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        self.vertex_valid(v1)
        self.vertex_valid(v2)
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for j in self.get_adjacent_vertices(i):
                print(i, '-->', j)


if __name__ == "__main__":
    g = AdjacencyMatrixGraph(4, directed=True)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print("Adjacent to: ", i, g.get_adjacent_vertices(i))

    for i in range(4):
        print("Indegree: ", i, g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

    g.display()
