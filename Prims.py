graph_dict = {  "a":{"b": 5, "d": 9, "e":2 },
                "b":{"a": 5, "c": 2},
                "c":{"b": 2, "d": 3},
                "d":{"a": 9, "c": 3, "f":2 },
                "e":{"a": 2, "f":3 },
                "f":{"d": 2, "e":3}
                }

g = {}
edges = {}
mst = []
#n = int(input(('Enter the number of nodes: ')))
n = 5
for i in graph_dict:
    g[i] = 99
src = input('Enter the source node: ')
edges[src] = 'None'
g[src] = 0
print(g)
while g:
    print('Map:  ',g)
    extract_min = list(min(zip(g.values(), g.keys())))
    print(extract_min)
    minimum_value  = extract_min[0]
    minimum_node = extract_min[1]
    print('Minimum-->',minimum_node)
    if edges[minimum_node]!='None':
        mst.append(edges[minimum_node])
    neighbours = [i for i in graph_dict[minimum_node].keys()]
    print('neighbours ',neighbours )
    for nei in neighbours:
        print('nei: ',nei)
        if nei in g.keys():
            if graph_dict[minimum_node][nei] < g[nei]:
                g[nei] = graph_dict[minimum_node][nei]
                edges[nei] = (minimum_node, nei)
    g.pop(minimum_node)


print('Minimum spanning tree: ',mst)