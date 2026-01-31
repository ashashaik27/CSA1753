import math

def tsp(graph, start=0):
    n = len(graph)
    ALL = 1 << n      # total subsets
    dp = [[math.inf] * n for _ in range(ALL)]
    
    # Start at `start` city
    dp[1 << start][start] = 0
    
    for mask in range(ALL):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v): 
                    continue
                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + graph[u][v])
    
    # Closing the cycle
    ans = math.inf
    for u in range(n):
        if u != start:
            ans = min(ans, dp[ALL-1][u] + graph[u][start])
    
    return ans


# Example graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Shortest TSP Tour Cost:", tsp(graph))
