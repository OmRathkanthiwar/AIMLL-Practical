import heapq

# DIJKSTRA ALGORITHM
def dijkstra(graph, start):

    distance = {}

    visited = set()

    for node in graph:
        distance[node] = float("inf")

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

                heapq.heappush(
                    priorityQueue,
                    (newDistance, neighbor)
                )

    return distance


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

distance = dijkstra(graph, start)


# DISPLAY RESULT
print("Shortest Distances")

for node in distance:

    print(start, "->", node, "=", distance[node])