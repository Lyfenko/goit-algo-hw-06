import networkx as nx
from create_and_visualize_graph import create_and_visualize_graph


def dijkstra_algorithm(graph):
    all_shortest_paths = {}
    nodes = list(graph.nodes())

    for start_node in nodes:
        shortest_paths = {}
        for end_node in nodes:
            if start_node != end_node:
                shortest_path = nx.shortest_path(
                    graph, source=start_node, target=end_node, weight="length"
                )
                shortest_distance = nx.shortest_path_length(
                    graph, source=start_node, target=end_node, weight="length"
                )
                shortest_paths[end_node] = {
                    "path": shortest_path,
                    "distance": shortest_distance,
                }

        all_shortest_paths[start_node] = shortest_paths

    return all_shortest_paths


def main():
    place_query = "Мала Березянка, Київська область, Україна"
    G = create_and_visualize_graph(place_query)

    all_shortest_paths = dijkstra_algorithm(G)

    # Виведення результатів
    for start_node, paths in all_shortest_paths.items():
        print(f"Найкоротші шляхи від вершини {start_node}:")
        for end_node, info in paths.items():
            print(f"  До вершини {end_node}:")
            print(f"    Шлях: {' -> '.join(map(str, info['path']))}")
            print(f"    Довжина: {info['distance']} метрів")
        print()


if __name__ == "__main__":
    main()
