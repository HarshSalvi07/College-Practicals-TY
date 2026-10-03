graph = {
    'src':[1,2,3],
    1:[4,5],
    2:[6],
    3:[7,8],
    4:[],
    5:[],
    6:[],
    7:['dest'],
    8:[],
    'dest':[]
}

h = {
    'src':20,
    1:22,
    2:21,
    3:10,
    4:25,
    5:24,
    6:30,
    7:5,
    8:12,
    'dest':0
}

open_list = ['src']
while open_list:
    node = open_list[0]
    for n in open_list:
        if h[n] < h[node]:
            node = n
    open_list.remove(node)
    print(node , end = " ")
    if node == 'dest':
        print("\n Goal Found")
        break
    open_list.extend(graph[node])