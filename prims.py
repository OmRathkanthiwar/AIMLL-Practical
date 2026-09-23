import heapq

# PRIM'S ALGORITHM
def prim(graph, start):

    visited = set()
    pq = []
    mstCost = 0

    visited.add(start)

    for neighbour, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbour))

    while pq:

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)
        mstCost += weight

        print(u, "->", v, "=", weight)

        for neighbour, w in graph[v]:

            if neighbour not in visited:
                heapq.heappush(pq, (w, v, neighbour))

    return mstCost


# INPUT GRAPH
n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):

    node = input("Vertex: ")
    graph[node] = []

    m = int(input("Number of neighbours: "))

    for j in range(m):

        neighbour = input("Neighbour: ")
        weight = int(input("Weight: "))

        graph[node].append((neighbour, weight))


# FIND MST
start = input("Enter starting vertex: ")

cost = prim(graph, start)

print("Minimum Cost of MST =", cost)