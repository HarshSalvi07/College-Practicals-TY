graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = []
stack = ['A']

while stack:
    node = stack.pop(0)

    if node not in visited:
        visited.append(node)
        stack.extend(reversed(graph[node]))
print(visited)