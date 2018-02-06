from queue import Queue
from graphs.graph_adj_matrix import AdjacencyMatrixGraph, Graph


def build_distrance_table(graph: Graph, source: int):
    distance_table = {}

    for i in range(graph.num_vertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbor][0] is None:
                distance_table[neighbor] = (1 + current_distance, current_vertex)

                if len(graph.get_adjacent_vertices(neighbor)) > 0:
                    queue.put(neighbor)

    return distance_table


def shortest_path(graph: Graph, source: int, destination: int):
    distance_table = build_distrance_table(graph, source)

    path = [destination]

    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print('No path from %d to %d' % (source, destination))
    else:
        path = [source] + path
        print('Shortest path is: ', path)


if __name__ == '__main__':
    g = AdjacencyMatrixGraph(8, directed=True)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(0, 7)

    shortest_path(g, 0, 5)
    shortest_path(g, 0, 6)
    shortest_path(g, 7, 4)
