import networkx as nx
from collections import defaultdict

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

def find_teleport_points(h, w, i, j, n):
    points = set()

    for di in range(-n, n + 1):
        for dj in range(-n, n + 1):
            if abs(di) + abs(dj) <= n:
                i2, j2 = i + di, j + dj
                if i2 >= 0 and i2 < h and j2 >= 0 and j2 < w:
                    points.add((i2, j2))
    return points

start  = ()
end    = ()
points = set()

G = nx.Graph()
for i, r in enumerate(l):
    for j, c in enumerate(r):
        if c == 'S':
            start = (i, j)
        elif c == 'E':
            end = (i, j)

        if c != '#':
            points.add((i, j))
            neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            for neighbour in neighbours:
                i2, j2      = neighbour
                neighbour_c = l[i2][j2]
                if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                    continue
                if neighbour_c != '#':
                    G.add_edge((i, j), neighbour)

# precompute distances from start node and to end node
distances_start = nx.single_source_shortest_path_length(G, source=start)
distances_end   = nx.single_source_shortest_path_length(G, source=end)

distance_no_cheat = distances_start[end]

max_jump   = 20
min_saving = 100
s          = 0
for point in points:
    # worth to cheat at this point?
    i, j = point
    teleports = find_teleport_points(h, w, i, j, max_jump)
    for point2 in teleports:
        if not point2 in points:
            continue
        i2, j2       = point2
        jump_length  = abs(i - i2) + abs(j - j2)
        new_distance = distances_start[point] + jump_length + distances_end[point2]
        if new_distance <= distance_no_cheat - min_saving:
            s += 1

print(s)