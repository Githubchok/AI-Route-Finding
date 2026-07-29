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

heuristic = {
    "Main Gate": 9,
    "Student Centre": 7,
    "Hostel": 8,
    "Cafeteria": 5,
    "Admin Office": 3,
    "Block A": 1,
    "Block B": 5,
    "Library": 0
}


def astar(graph, start, goal, verbose=False):
    start_time = time.perf_counter()
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}
    nodes_expanded = 0

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited and visited[current] <= g:
            continue
        visited[current] = g
        nodes_expanded += 1

        if current == goal:
            end_time = time.perf_counter()
            return path, g, nodes_expanded, end_time - start_time

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_h = heuristic[neighbor]
            new_f = new_g + new_h

            if verbose:
                print(f"{current} -> {neighbor}: f(n) = {new_g} + {new_h} = {new_f}")

            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None  # no path found


if __name__ == "__main__":
    result = astar(graph, "Main Gate", "Library")
    if result is None:
        print("No route found.")
    else:
        path, total_cost, expanded_nodes, execution_time = result
        print("===== A* Search Result =====")
        print("Optimal Route :", " -> ".join(path))
        print("Path Cost     :", total_cost)
        print("Nodes Expanded:", expanded_nodes)
        print(f"Execution Time: {execution_time:.6f} seconds")