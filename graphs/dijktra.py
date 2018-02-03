from graphs.priority_queue import PriorityDict
from graphs.graph_adj_matrix import AdjacencyMatrixGraph, Graph


def build_distance_table(graph: Graph, source: int):
    distance_table = {}

    for i in range(graph.num_vertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)

    prio_queue = PriorityDict()
    prio_queue[source] = 0

    while len(prio_queue.keys()) > 0:
        current_vertex = prio_queue.pop_smallest()

        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(current_vertex, neighbor)
            old_distance = distance_table[neighbor][0]

            if old_distance is None or old_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                prio_queue[neighbor] = distance

    return distance_table


def shortest_path(graph: Graph, source: int, destination: int):
    distance_table = build_distance_table(graph, source)

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
    g = AdjacencyMatrixGraph(8, directed=False)

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(5, 4, 5)
    g.add_edge(3, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(0, 7, 8)

    shortest_path(g, 0, 6)
    shortest_path(g, 4, 7)
    shortest_path(g, 7, 0)
