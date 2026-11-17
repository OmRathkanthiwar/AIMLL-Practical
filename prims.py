import heapq

# PRIM'S ALGORITHM
def prim(graph, start):

    visited = set()
    pq = []
    mstCost = 0
    edges = []

    visited.add(start)

    for neighbour, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbour))

    while pq and len(visited) < len(graph):

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)
        mstCost += weight
        edges.append((u, v, weight))

        for neighbour, w in graph[v]:
            if neighbour not in visited:
                heapq.heappush(pq, (w, v, neighbour))

    # DISPLAY MST
    if len(visited) != len(graph):
        print("\nMST cannot be formed. Graph is disconnected.")
        return

    print("\nSelected MST Edges:")

    for u, v, weight in edges:
        print(u, "->", v, "=", weight)

    print("\nNumber of Edges:", len(edges))
    print("Minimum Cost of MST =", mstCost)

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

if start in graph:
    prim(graph, start)
else:
    print("Invalid starting vertex")