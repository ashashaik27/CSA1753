from collections import deque

# Check whether a state is valid
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

# BFS solution
def solve_missionaries_cannibals():
    start = (3, 3, 0, 0, 'L')  # (M_left, C_left, M_right, C_right, Boat)
    goal = (0, 0, 3, 3, 'R')

    queue = deque()
    queue.append((start, []))
    visited = set()
\=*
    while queue:
        (state, path) = queue.popleft()
        m_left, c_left, m_right, c_right, boat = state

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        if boat == 'L':  # Boat on left side
            moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
            for m, c in moves:
                new_state = (
                    m_left - m, c_left - c,
                    m_right + m, c_right + c,
                    'R'
                )
                if is_valid(*new_state[:4]):
                    queue.append((new_state, path + [state]))
        else:  # Boat on right side
            moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
            for m, c in moves:
                new_state = (
                    m_left + m, c_left + c,
                    m_right - m, c_right - c,
                    'L'
                )
                if is_valid(*new_state[:4]):
                    queue.append((new_state, path + [state]))

    return None

# Main program
if __name__ == "__main__":
    solution = solve_missionaries_cannibals()

    if solution:
        print("Solution steps:\n")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
