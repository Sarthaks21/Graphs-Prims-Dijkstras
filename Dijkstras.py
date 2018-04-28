graph_dict = {  "a":{"b": 5, "d": 9, "e":2 },
                "b":{"a": 5, "c": 2},
                "c":{"b": 2, "d": 3},
                "d":{"a": 9, "c": 3, "f":2 },
                "e":{"a": 2, "f":3 },
                "f":{"d": 2, "e":3}
                }

g = {}
parent = {}
distance = {}
#n = int(input(('Enter the number of nodes: ')))
n = 5
for i in graph_dict:
    g[i] = 99
    distance[i] = 99
src = input('Enter the source node: ')
g[src] = 0
distance[src] = 0
parent[src] = 'None'
print(g)
while g:
    print('Map:  ',g)
    extract_min = list(min(zip(g.values(), g.keys())))
    minimum_value  = extract_min[0]
    minimum_node = extract_min[1]
    print('Minimum-->',minimum_node)
    neighbours = [i for i in graph_dict[minimum_node].keys()]
    print('neighbours ',neighbours )
    for nei in  neighbours:
        print('nei: ',nei)
        if nei in g.keys():
            new_dist = distance[minimum_node] + graph_dict[minimum_node][nei]
            if new_dist < distance[nei]:
                g[nei] = new_dist
                distance[nei] = new_dist
                parent[nei] = minimum_node
    g.pop(minimum_node)

print('Distance:    ',distance)
dest = input('Enter the destination node: ')
ar = []
ar.append(dest)
p = parent[dest]
while parent[p]!='None':
    ar.append(p)
    p = parent[p]
ar.append(src)
ar.reverse()
print('Path:     ',ar)
print('Distance', distance[dest])