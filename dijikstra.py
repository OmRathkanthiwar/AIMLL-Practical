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

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:

        currentDistance, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        for neighbour, weight in graph[current]:

            newDistance = currentDistance + weight

            if newDistance < distance[neighbour]:

                distance[neighbour] = newDistance
                previous[neighbour] = current

                heapq.heappush(pq, (newDistance, neighbour))

    return distance, previous


# DISPLAY SHORTEST PATH
def display(graph, start, distance, previous):

    print("\nShortest Distances and Paths:")

    for node in graph:

        if distance[node] == float("inf"):
            print(node, ": No path exists")
            continue

        path = []
        current = node

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        print("Path:", " -> ".join(path))
        print("Distance:", distance[node])


# INPUT GRAPH
n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):

    node = input("Enter vertex: ")
    graph[node] = []

    m = int(input("Enter number of connected vertices: "))

    for j in range(m):

        neighbour = input("Enter connected vertex: ")
        weight = int(input("Enter edge weight: "))

        graph[node].append((neighbour, weight))


# FIND SHORTEST PATH
start = input("Enter starting vertex: ")

if start in graph:

    distance, previous = dijkstra(graph, start)

    display(graph, start, distance, previous)

else:
    print("Invalid starting vertex")
