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

def area_perimeter(m, region, c):
    a = len(region)
    p = 0
    for (i, j) in region:
        neighbours = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        
        for neighbour in neighbours:
            i2, j2 = neighbour
            if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                p += 1
            elif m[(i2, j2)] != c:
                p += 1
    
    return (a, p)



visited = set()

price = 0
for i in range(h):
    for j in range(w):
        pos = (i, j)
        if not (i, j) in visited:
            c      = m[pos]
            region = flood_fill(m, pos, visited, c)
            a, p   = area_perimeter(m, region, c)
            price  += a * p

print(price)