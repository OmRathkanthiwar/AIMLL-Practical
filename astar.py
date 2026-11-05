import heapq

# MANHATTAN DISTANCE
def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goalIndex = goal.index(state[i])

            x1, y1 = i // 3, i % 3
            x2, y2 = goalIndex // 3, goalIndex % 3

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

# A* SEARCH
def solve(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dx, dy, move in moves:
            newRow = row + dx
            newCol = col + dy

            if 0 <= newRow < 3 and 0 <= newCol < 3:
                newIndex = newRow * 3 + newCol

                newState = state.copy()
                newState[zero], newState[newIndex] = newState[newIndex], newState[zero]

                if tuple(newState) not in visited:
                    newG = g + 1
                    newF = newG + heuristic(newState, goal)

                    heapq.heappush(
                        pq,
                        (newF, newG, newState, path + [state])
                    )

    return None

# TAKE USER INPUT
print("Enter initial state (use 0 for blank):")
start = []

for i in range(9):
    start.append(int(input("Enter value: ")))

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# SOLVE PUZZLE
result = solve(start, goal)

# DISPLAY SOLUTION
if result:
    print("\nSolution found!")
    print("Total Moves:", len(result) - 1)

    for i, state in enumerate(result):
        print("\nStep", i)
        for j in range(0, 9, 3):
            print(state[j:j+3])
else:
    print("No solution exists.")