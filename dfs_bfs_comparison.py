from collections import deque
from create_and_visualize_graph import create_and_visualize_graph


def dfs(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs(graph, neighbor, end, path + [neighbor])
            paths.extend(new_paths)
    return paths


def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path
                queue.append((neighbor, new_path))
    return None


def main():
    place_query = "Мала Березянка, Київська область, Україна"
    G = create_and_visualize_graph(place_query)

    start_node = next(iter(G.nodes()))
    end_node = list(G.nodes())[-1]

    dfs_paths = dfs(G, start_node, end_node)
    bfs_path = bfs(G, start_node, end_node)

    print("DFS paths:", dfs_paths)
    print("BFS path:", bfs_path)


if __name__ == "__main__":
    main()
