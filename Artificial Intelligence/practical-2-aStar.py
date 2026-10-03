graph = {
    'S':[('A',7),('B',2),('C',3)],
    'A':[('B',3),('D',4)],
    'B':[('D',4),('H',1)],
    'C':[('L',2)],
    'D':[('F',5)],
    'H':[('F',3),('G',2)],
    'L':[('I',4),('J',4)],
    'I':[('K',4)],
    'J':[('K',4)],
    'G':[('E',2)],
    'K':[('E',5)]
}

h = {
    'S':10, 'A':9, 'B':7, 'C':8,
    'D':8, 'F':6, 'H':6, 'G':3,
    'L':6, 'T':4, 'J':4, 'K':3,
    'E':0
}

open = [('S',0)]
closed = []
while open:
    best = open[0]
    for i in open:
        if i[1] + h[i[0]] < best[1] + h[best[0]]:
            best = i
    open.remove(best)
    node = best[0]
    g = best[1]
    print(node , end = " ")
    if node == 'E':
        print("\n Goal Found")
        print("Cost = ",g)
        break
    closed.append(node)
    if node in graph:
        for child, cost in graph[node]:
            if child not in closed:
                open.append((child,g+cost))