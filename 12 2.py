with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

m = {}

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c

def flood_fill(m, pos, visited, c):
    positions = []
    Q         = [pos]
    while len(Q) > 0:
        cur_pos = Q.pop(0)
        if cur_pos in visited:
            continue

        if m[cur_pos] == c:
            visited.add(cur_pos)
            positions.append(cur_pos)
            i, j = cur_pos
            neighbours = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            for neighbour in neighbours:
                i2, j2 = neighbour
                if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                    continue
                Q.append(neighbour)

    return positions

def area_sides(region):
    a = len(region)
    s = n_corners(region)

    return (a, s)

# find number of corners (= number of sides) of region
def n_corners(region):
    corners = 0

    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for (i, j) in region:
        for dir_i in range(len(dirs)):
            di, dj   = dirs[dir_i]
            di2, dj2 = dirs[(dir_i + 1) % 4]
            i2, j2 = i + di, j + dj
            i3, j3 = i + di2, j + dj2
            i4, j4 = i + di + di2, j + dj + dj2
            if (i2, j2) not in region and (i3, j3) not in region:
                corners += 1
            elif (i2, j2) in region and (i3, j3) in region and (i4, j4) not in region:
                corners += 1
    
    return corners

visited = set()

price = 0
for i in range(h):
    for j in range(w):
        pos = (i, j)
        if not (i, j) in visited:
            c      = m[pos]
            region = flood_fill(m, pos, visited, c)
            a, s   = area_sides(region)
            price  += a * s

print(price)