from heapq import heappush, heappop

# Goal state of the puzzle
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible moves (Up, Down, Left, Right)
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Manhattan distance heuristic
def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL_STATE.index(state[i])
            distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

# Generate next possible states
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    for move in MOVES[zero_index]:
        new_state = list(state)
        new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
        neighbors.append(tuple(new_state))
    return neighbors

# A* algorithm
def solve_puzzle(start_state):
    priority_queue = []
    heappush(priority_queue, (manhattan(start_state), 0, start_state, []))
    visited = set()

    while priority_queue:
        f, g, current, path = heappop(priority_queue)

        if current == GOAL_STATE:
            return path + [current]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heappush(priority_queue,
                         (g + 1 + manhattan(neighbor),
                          g + 1,
                          neighbor,
                          path + [current]))

    return None

# Display the puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Main program
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    solution = solve_puzzle(start_state)

    if solution:
        print("Solution steps:\n")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
