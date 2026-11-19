
import heapq

# WEIGHTED GRAPH
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5)],
    'C': [('A', 2), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

start = 'A'
goal = 'F'

# HEURISTIC VALUES
h = {
    'A': 10,
    'B': 8,
    'C': 10,
    'D': 5,
    'E': 3,
    'F': 0
}

# A* ALGORITHM
def astar():

    pq = [(h[start], 0, start)]

    g_cost = {start: 0}
    parent = {}

    while pq:

        f, g, current = heapq.heappop(pq)

        if current == goal:
            break

        if g > g_cost[current]:
            continue

        # CHECK NEIGHBOURS
        for neighbor, weight in graph[current]:

            new_g = g + weight

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + h[neighbor]

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


astar()
