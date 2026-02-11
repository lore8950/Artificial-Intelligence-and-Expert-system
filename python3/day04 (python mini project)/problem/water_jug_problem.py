from collections import deque

# Capacity of jugs
JUG1 = 4
JUG2 = 3
GOAL = 2

def water_jug_bfs():
    start = (0, 0)
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if x == GOAL:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Possible moves
        next_states = []

        # Fill Jug1
        next_states.append((JUG1, y))

        # Fill Jug2
        next_states.append((x, JUG2))

        # Empty Jug1
        next_states.append((0, y))

        # Empty Jug2
        next_states.append((x, 0))

        # Pour Jug1 -> Jug2
        pour = min(x, JUG2 - y)
        next_states.append((x - pour, y + pour))

        # Pour Jug2 -> Jug1
        pour = min(y, JUG1 - x)
        next_states.append((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    return None


# Run
solution = water_jug_bfs()

if solution:
    print("Solution Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
