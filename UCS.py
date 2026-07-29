import heapq
import time

def add_edge(g, a, b, cost):
    g.setdefault(a, []).append((b, cost))
    g.setdefault(b, []).append((a, cost))

graph = {}
add_edge(graph, "Main Gate", "Student Centre", 4)
add_edge(graph, "Main Gate", "Hostel", 3)
add_edge(graph, "Student Centre", "Cafeteria", 3)
add_edge(graph, "Hostel", "Block B", 5)
add_edge(graph, "Cafeteria", "Admin Office", 5)
add_edge(graph, "Cafeteria", "Block B", 2)
add_edge(graph, "Admin Office", "Block A", 2)
add_edge(graph, "Admin Office", "Library", 4)
add_edge(graph, "Block A", "Library", 3)
add_edge(graph, "Block A", "Block B", 4)


def ucs(graph, start, goal):
    start_time = time.perf_counter()
    priority_queue = [(0, start, [start])]
    visited = set()
    expanded_nodes = 0

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue
        visited.add(node)
        expanded_nodes += 1

        if node == goal:
            end_time = time.perf_counter()
            return path, cost, expanded_nodes, end_time - start_time

        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbour, path + [neighbour]))

    return None  # no path found


if __name__ == "__main__":
    result = ucs(graph, "Main Gate", "Library")
    if result is None:
        print("No route found.")
    else:
        path, total_distance, expanded_nodes, execution_time = result
        print("===== UCS Result =====")
        print("Optimal Route:", " -> ".join(path))
        print("Total Distance:", total_distance)
        print("Expanded Nodes:", expanded_nodes)
        print(f"Execution Time: {execution_time:.6f} seconds")