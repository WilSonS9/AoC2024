import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

m            = {}
trailheads   = []
destinations = []

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c
        if c != '.':
            height  = int(c)
            m[(i, j)] = height
            if height == 0:
                trailheads.append((i, j))
            elif height == 9:
                destinations.append((i, j))

G = nx.DiGraph()
for (i, j), height in m.items():
    neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for (i2, j2) in neighbours:
        if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
            continue
        height2 = m[(i2, j2)]
        if height2 - height == 1:
            G.add_edge((i, j), (i2, j2))

s = 0

for trailhead in trailheads:
    for destination in destinations:
        s += len(list(nx.all_simple_paths(G,trailhead,destination)))

print(s)