def bfs(graph, node):
    visited = {}
    for vertice in graph['vertices']:
        visited[vertice] = False

    queue = [node]
    visited[node] = True
    edges = list(graph['edges'])
    while queue:
        s = queue.pop(0)
        for edge in edges:
            w, x1, x2 = edge
            if s == x1:
                if not visited[x2]:
                    queue.append(x2)
                    visited[x2] = True
            elif s == x2:
                if not visited[x1]:
                    queue.append(x1)
                    visited[x1] = True
    return visited
