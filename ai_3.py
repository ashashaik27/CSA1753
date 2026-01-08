from collections import deque

def water_jug(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # (jug1, jug2, path)
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        # Possible operations
        states = [
            (jug1_capacity, jug2),             # Fill jug1
            (jug1, jug2_capacity),             # Fill jug2
            (0, jug2),                          # Empty jug1
            (jug1, 0),                          # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2),
             jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, jug1_capacity - jug1),
             jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 -> jug1
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None

# Main program
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    solution = water_jug(jug1_capacity, jug2_capacity, target)

    if solution:
        print("Steps to reach the target:\n")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
