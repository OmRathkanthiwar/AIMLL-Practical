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
m = int(input("Enter number of edges: "))

edges = []
vertices = []

for i in range(m):

    u = input("Vertex 1: ")
    v = input("Vertex 2: ")
    w = int(input("Weight: "))

    edges.append((w, u, v))

    if u not in vertices:
        vertices.append(u)

    if v not in vertices:
        vertices.append(v)


# SORT EDGES
edges.sort()

parent = []
rank = []

for i in range(len(vertices)):
    parent.append(i)
    rank.append(0)


# KRUSKAL'S ALGORITHM
cost = 0
edgeCount = 0

for w, u, v in edges:

    uIndex = vertices.index(u)
    vIndex = vertices.index(v)

    if union(parent, rank, uIndex, vIndex):

        print(u, "-", v, "=", w)

        cost += w
        edgeCount += 1

        if edgeCount == len(vertices) - 1:
            break


print("Minimum Cost of MST =", cost)