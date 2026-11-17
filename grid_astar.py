
import heapq

# MANHATTAN DISTANCE
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* SEARCH
def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start))

    distance = {start: 0}
    previous = {}

    visited = set()

    while pq:

        f, g, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        row, col = current

        moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dx, dy in moves:

            newRow = row + dx
            newCol = col + dy

            if (0 <= newRow < rows and
                0 <= newCol < cols and
                grid[newRow][newCol] == 0):

                neighbour = (newRow, newCol)

                newG = g + 1

                if newG < distance.get(neighbour, float("inf")):

                    distance[neighbour] = newG
                    previous[neighbour] = current

                    newF = newG + heuristic(neighbour, goal)

                    heapq.heappush(
                        pq, (newF, newG, neighbour)
                    )

    # DISPLAY PATH
    if goal not in distance:
        print("No path exists")
        return

    path = []
    current = goal

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    print("\nOptimal Path:")

    for point in path:
        print(point)

    print("Traversal Cost:", distance[goal])


# INPUT GRID
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid (0 = Free, 1 = Obstacle):")

for i in range(rows):

    row = []

    for j in range(cols):
        value = int(input("Enter value: "))
        row.append(value)

    grid.append(row)


# START AND GOAL
print("\nEnter start coordinates:")
sx = int(input("Row: "))
sy = int(input("Column: "))

print("\nEnter goal coordinates:")
gx = int(input("Row: "))
gy = int(input("Column: "))

start = (sx, sy)
goal = (gx, gy)

# SOLVE PATH
if (0 <= sx < rows and 0 <= sy < cols and
    0 <= gx < rows and 0 <= gy < cols and
    grid[sx][sy] == 0 and grid[gx][gy] == 0):

    astar(grid, start, goal)

else:
    print("Invalid start or goal position")
