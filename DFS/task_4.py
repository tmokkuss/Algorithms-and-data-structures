def find_components(graph):
    def dfs(node, component):
        component.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

edges = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8)]
graph = {}

for edge in edges:
    u, v = edge
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

components = find_components(graph)

for component in components:
    print(component)
