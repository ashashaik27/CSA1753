import heapq

def a_star(graph, start, goal, heuristic):
    pq = []  # priority queue
    heapq.heappush(pq, (0, start))

    came_from = {start: None}
    g_cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_cost, neighbor))
                came_from[neighbor] = current

    return None, float("inf")
# Graph (Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Simple heuristic (straight-line guess)
def heuristic(n1, n2):
    H = {
        ('A', 'D'): 7,
        ('B', 'D'): 5,
        ('C', 'D'): 1,
        ('D', 'D'): 0
    }
    return H[(n1, n2)]

path, cost = a_star(graph, 'A', 'D', heuristic)
print("Path:", path)
print("Cost:", cost)
