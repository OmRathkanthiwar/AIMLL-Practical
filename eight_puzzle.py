from queue import PriorityQueue

goal = ((1,2,3), (4,5,6), (7,8,0))

# MANHATTAN DISTANCE
def heuristic(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                x = (value-1) // 3
                y = (value-1) % 3

                distance += abs(i-x) + abs(j-y)

    return distance


# GENERATE NEIGHBOURS
def get_neighbors(state):
    neighbors = []

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                moves = [(-1,0), (1,0), (0,-1), (0,1)]

                for dx, dy in moves:
                    x = i+dx
                    y = j+dy

                    if 0 <= x < 3 and 0 <= y < 3:
                        new_state = [list(row) for row in state]
                        new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
                        neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


# PRINT PATH
def print_path(parent, state):
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for state in path:
        for row in state:
            print(row)
        print()


# A* ALGORITHM
def astar(start):
    pq = PriorityQueue()

    pq.put((heuristic(start), 0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while not pq.empty():

        f, g, current = pq.get()

        if current == goal:
            print("Goal Reached!")
            print("Total Moves:", g)
            print_path(parent, current)
            return

        if g > g_cost[current]:
            continue

        for neighbor in get_neighbors(current):

            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic(neighbor)

                pq.put((new_f, new_g, neighbor))

    print("No Solution Exists")


# START STATE
start = ((1,2,3), (4,0,6), (7,5,8))

astar(start)
