import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

nodes = set()
start = ()
end   = ()

for i, r in enumerate(l):
    for j, c in enumerate(r):
        if c != '#':
            nodes.add((i, j))
        if c == 'S':
            start = (i, j)
        elif c == 'E':
            end = (i, j)

directions   = {0: 'north', 1: 'east', 2: 'south', 3: 'west'}
n_directions = len(directions)

G = nx.DiGraph()
for (i, j) in nodes:
    neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
    for neighbour_index, (i2, j2) in enumerate(neighbours):
        if not (i2, j2) in nodes:
            continue
        G.add_edge((i, j, directions[neighbour_index]), (i2, j2, directions[neighbour_index]), weight=1)
    for dir_i in range(n_directions):
        G.add_edge((i, j, directions[dir_i]), (i, j, directions[(dir_i + 1) % n_directions]), weight=1000) # clockwise
        G.add_edge((i, j, directions[dir_i]), (i, j, directions[(dir_i - 1) % n_directions]), weight=1000) # counterclockwise


lengths = []
for direction in directions.values():
    path = nx.shortest_path(G, source=(start[0], start[1], 'east'), target=(end[0], end[1], direction), weight='weight')
    path_length = nx.shortest_path_length(G, source=(start[0], start[1], 'east'), target=(end[0], end[1], direction), weight='weight')
    lengths.append(path_length)

print(min(lengths))