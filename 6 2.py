with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = {}
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # list of all direction deltas, ordered by clockwise rotation

cur_pos = (0, 0)
cur_dir = 0

h = len(l)
w = len(l[0])

def has_loop(m, cur_pos, cur_dir, part_1): # set part_1 to `True` to return `visited`
    previous = set()
    visited = set()

    if m[cur_pos] == '#':
        # cannot place obstacle on starting position
        return False

    while True:
        i, j      = cur_pos
        di, dj    = dirs[cur_dir]
        cur_state = ((i, j), cur_dir)
        if cur_state in previous:
            return True

        previous.add(cur_state)
        visited.add(cur_pos)

        new_i, new_j = i + di, j + dj
        if new_i < 0 or new_i >= w or new_j < 0 or new_j >= h:
            if part_1:
                return visited
            return False

        new_c = m[(new_i, new_j)]
        if new_c == '.':
            cur_pos = (new_i, new_j)
        else:
            cur_dir = (cur_dir + 1) % len(dirs)

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c
        if c == '^':
            cur_pos = (i, j)
            m[(i, j)] = '.'

visited = has_loop(m, cur_pos, cur_dir, True)

s = 0

for (i, j) in visited:
    if m[(i, j)] != '.':
        continue

    new_m = m.copy()
    new_m[(i, j)] = '#'
    if has_loop(new_m, cur_pos, cur_dir, False):
        s += 1

print(s)