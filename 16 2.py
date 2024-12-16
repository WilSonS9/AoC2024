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


min_weight = 100000000
min_paths  = []
for direction in directions.values():
    # all shortest paths that end in the given direction
    paths       = list(nx.all_shortest_paths(G, source=(start[0], start[1], 'east'), target=(end[0], end[1], direction), weight='weight'))
    path_weight = nx.path_weight(G, paths[0], weight='weight')

    # if two sets of paths have the same (minimal) score but with different end directions, keep both
    if path_weight == min_weight:
        for path in paths:
            min_paths.append(path)
    elif path_weight < min_weight:
        min_weight = path_weight
        min_paths  = list(paths)[:]

tiles = set()
for path in min_paths:
    for (i, j, _) in path:
        tiles.add((i, j))

print(len(tiles))