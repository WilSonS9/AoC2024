with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = {}

h = len(l)
w = len(l[0])

antennae = []

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c
        if c != '.':
            antennae.append(((i, j), c))

antinode_locations = set()

for a1_index, ((i1, j1), c1) in enumerate(antennae):
    for (i2, j2), c2 in antennae[a1_index + 1:]:
        if c1 != c2:
            continue

        di = i2 - i1
        dj = j2 - j1
        antinode_1 = (i1 - di, j1 - dj)
        antinode_2 = (i2 + di, j2 + dj)
        antinodes = [antinode_1, antinode_2]

        for antinode in antinodes:
            i, j = antinode
            if i < 0 or i >= h or j < 0 or j >= w:
                continue
            antinode_locations.add(antinode)

print(len(antinode_locations))