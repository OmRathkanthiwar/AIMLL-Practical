import heapq

# DIJKSTRA ALGORITHM
def dijkstra(graph, start):

    distance = {}
    previous = {}
    visited = set()

    for node in graph:
        distance[node] = float("inf")
        previous[node] = None

    distance[start] = 0

    priorityQueue = []
    heapq.heappush(priorityQueue, (0, start))

    while priorityQueue:

        currentDistance, current = heapq.heappop(priorityQueue)

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current]:

            newDistance = currentDistance + weight

            if newDistance < distance[neighbor]:

                distance[neighbor] = newDistance
                previous[neighbor] = current

                heapq.heappush(
                    priorityQueue,
                    (newDistance, neighbor)
                )

    return distance, previous


# INPUT GRAPH
n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):

    node = input("Enter vertex: ")
    graph[node] = []

    m = int(input("Enter number of connected vertices: "))

    for j in range(m):

        neighbor = input("Enter connected vertex: ")
        weight = int(input("Enter edge weight: "))

        graph[node].append((neighbor, weight))


# FIND SHORTEST PATH
start = input("Enter starting vertex: ")

if start in graph:

    distance, previous = dijkstra(graph, start)

    # DISPLAY RESULT
    print("\nShortest Distances and Paths:")

    for node in graph:

        if distance[node] == float("inf"):
            print(start, "->", node, "= No path exists")
            continue

        path = []
        current = node

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        print("Path:", " -> ".join(path))
        print("Distance:", distance[node])
        print()

else:
    print("Invalid starting vertex")
