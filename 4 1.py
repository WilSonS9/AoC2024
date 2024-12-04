import itertools

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = [[c for c in r] for r in l]
h = len(m)
w = len(m[0])

def starts_xmas(m, h, w, i, j):
    s = 0

    dirs = list(itertools.product([0, 1, -1], [0, 1, -1]))[1:] # first element is (0, 0); not a valid search direction
    for dir in dirs:
        s += search_direction(m, h, w, i, j, dir)

    return s

def search_direction(m, h, w, i, j, dir):
    'returns `1` if there is an XMAS starting at `(i, j)` going in direction `dir`, else `0`'

    goal      = 'XMAS'
    cur       = 'X'
    cur_index = 1

    d_i, d_j = dir

    i += d_i
    j += d_j

    while i >= 0 and i < h and j >= 0 and j < w:
        new_char = m[i][j]
        if new_char == goal[cur_index]:
            cur       += new_char
            cur_index += 1
            if cur == goal:
                return 1
            i += d_i
            j += d_j
        else:
            return 0

    return 0

total_s = 0

for i, r in enumerate(l):
    for j, c in enumerate(r):
        if c == 'X':
            total_s += starts_xmas(m, h, w, i, j)

print(total_s)
