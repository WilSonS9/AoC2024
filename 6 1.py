with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = {}
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # list of all direction deltas, ordered by clockwise rotation

cur_pos = (0, 0)
cur_dir = 0

h = len(l)
w = len(l[0])

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c
        if c == '^':
            cur_pos = (i, j)
            m[(i, j)] = '.'

visited = set()

while True:
    i, j   = cur_pos
    di, dj = dirs[cur_dir]
    visited.add((i, j))

    new_i, new_j = i + di, j + dj
    if new_i < 0 or new_i >= w or new_j < 0 or new_j >= h:
        break

    new_c = m[(new_i, new_j)]
    if new_c == '.':
        cur_pos = (new_i, new_j)
    else:
        cur_dir = (cur_dir + 1) % len(dirs)

print(len(visited))