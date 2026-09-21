# Graph:
#
#       0
#      / \
#     1---2
#          \
#           3
#
# Edges:
# 0 -- 1
# 0 -- 2
# 1 -- 2
# 2 -- 3


# --------------------------------------------------
# 1. ADJACENCY MATRIX
# --------------------------------------------------

vertices = 4

matrix = [[0] * vertices for _ in range(vertices)]

edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3)
]

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1       # Undirected graph

print("Adjacency Matrix:")
for row in matrix:
    print(row)


# --------------------------------------------------
# 2. ADJACENCY LIST
# --------------------------------------------------

adj_list = [[] for _ in range(vertices)]

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print("\nAdjacency List:")
for vertex in range(vertices):
    print(vertex, "->", adj_list[vertex])


# --------------------------------------------------
# 3. ADJACENCY DICTIONARY
# --------------------------------------------------

adj_dict = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print("\nAdjacency Dictionary:")
for vertex, neighbours in adj_dict.items():
    print(vertex, "->", neighbours)