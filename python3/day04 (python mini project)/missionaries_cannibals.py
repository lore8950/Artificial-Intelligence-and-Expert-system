from collections import deque

def is_valid(state):
    M, C, _ = state
  
    if M < 0 or C < 0 or M > 3 or C > 3:
        return False

    if M > 0 and C > M:
        return False

    M_right = 3 - M
    C_right = 3 - C

    if M_right > 0 and C_right > M_right:
        return False

    return True


# Generate all possible next states
def get_next_states(state):
    M, C, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    next_states = []

    for m, c in moves:
        if boat == 0:  # Left to Right
            new_state = (M - m, C - c, 1)
        else:          # Right to Left
            new_state = (M + m, C + c, 0)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


# BFS
def solve_missionaries_cannibals():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for next_state in get_next_states(current):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None


# run the program
solution = solve_missionaries_cannibals()

if solution:
    print("Solution Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
