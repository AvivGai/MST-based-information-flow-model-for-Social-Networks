parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph, num_of_v):
    edges_counter = 0
    index = 0
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    while edges_counter < num_of_v-1:
        weight, vertice1, vertice2 = edges[index]
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edges[index])
            edges_counter = edges_counter+1
        index = index+1
    return sorted(minimum_spanning_tree)