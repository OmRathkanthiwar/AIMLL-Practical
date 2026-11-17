# FIND ROOT
def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


# UNION
def union(parent, rank, x, y):

    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX == rootY:
        return False

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY

    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX

    else:
        parent[rootY] = rootX
        rank[rootX] += 1

    return True


# INPUT GRAPH
n = int(input("Enter number of vertices: "))

vertices = []

for i in range(n):
    vertex = input("Enter vertex: ")
    vertices.append(vertex)

m = int(input("Enter number of edges: "))

edges = []

for i in range(m):

    u = input("Vertex 1: ")
    v = input("Vertex 2: ")
    w = int(input("Weight: "))

    edges.append((w, u, v))


# SORT EDGES
edges.sort()

print("\nSorted Edges:")

for w, u, v in edges:
    print(u, "-", v, "=", w)


# INITIALIZE DISJOINT SET
parent = []
rank = []

for i in range(n):
    parent.append(i)
    rank.append(0)


# KRUSKAL'S ALGORITHM
cost = 0
edgeCount = 0
mst = []

print("\nCycle Checks:")

for w, u, v in edges:

    uIndex = vertices.index(u)
    vIndex = vertices.index(v)

    if union(parent, rank, uIndex, vIndex):

        print(u, "-", v, "=", w, "-> No Cycle (Accepted)")

        mst.append((u, v, w))
        cost += w
        edgeCount += 1

        if edgeCount == n - 1:
            break

    else:
        print(u, "-", v, "=", w, "-> Cycle Detected (Rejected)")


# DISPLAY MST
if edgeCount == n - 1:

    print("\nSelected MST Edges:")

    for u, v, w in mst:
        print(u, "-", v, "=", w)

    print("Total Minimum Cost =", cost)

else:
    print("\nMST cannot be formed. Graph is disconnected.")
