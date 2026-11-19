import heapq

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# HEURISTIC
def heuristic(node):
    return abs(node[0]-goal[0]) + abs(node[1]-goal[1])


# A* ALGORITHM
def astar():
    pq = [(heuristic(start), 0, start)]

    g_cost = {start: 0}
    parent = {}

    while pq:

        f, g, current = heapq.heappop(pq)

        if current == goal:
            break

        if g > g_cost[current]:
            continue

        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in moves:
            x = current[0] + dx
            y = current[1] + dy

            neighbor = (x, y)

            if (0 <= x < len(grid) and
                0 <= y < len(grid[0]) and
                grid[x][y] == 0):

                new_g = g + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:

                    g_cost[neighbor] = new_g
                    parent[neighbor] = current

                    new_f = new_g + heuristic(neighbor)

                    heapq.heappush(pq, (new_f, new_g, neighbor))

    else:
        print("No Path Found")
        return

    # RECONSTRUCT PATH
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    print("Shortest Path:", path)
    print("Total Cost:", g_cost[goal])

    # DISPLAY GRID
    for x, y in path:
        if (x, y) != start and (x, y) != goal:
            grid[x][y] = "*"

    for row in grid:
        print(row)


astar()
