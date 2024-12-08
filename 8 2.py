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

        # antinodes in direction d2 - d1
        i = 0
        while True:
            new_i = i1 - i * di
            new_j = j1 - i * dj
            if new_i < 0 or new_i >= h or new_j < 0 or new_j >= w:
                break
            antinode_locations.add((new_i, new_j))
            i += 1
        
        # antinodes in direction d1 - d2
        i = 0
        while True:
            new_i = i2 + i * di
            new_j = j2 + i * dj
            if new_i < 0 or new_i >= h or new_j < 0 or new_j >= w:
                break
            antinode_locations.add((new_i, new_j))
            i += 1

print(len(antinode_locations))