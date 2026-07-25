import heapq
import time

# Graph with edge costs
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

# Heuristic values
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


def astar(start, goal):
    start_time = time.perf_counter()

    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))

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

            print("\n===== A* Search Result =====")
            print("Optimal Route :", " -> ".join(path))
            print("Path Cost     :", g)
            print("Nodes Expanded:", nodes_expanded)
            print(f"Execution Time: {end_time - start_time:.6f} seconds")
            return

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_h = heuristic[neighbor]
            new_f = new_g + new_h

            print(f"{current} -> {neighbor}: f(n) = {new_g} + {new_h} = {new_f}")

            heapq.heappush(
                pq,
                (new_f, new_g, neighbor, path + [neighbor])
            )


astar("Main Gate", "Library")