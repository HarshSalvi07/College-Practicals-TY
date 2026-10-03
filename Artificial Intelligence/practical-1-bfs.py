graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = []
queue = ['A']

while queue:
    node = queue.pop(0)

    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])

print(visited)