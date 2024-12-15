from collections import defaultdict

with open('inp.txt', 'r') as f:
    l, instructions = f.read().split('\n\n')

# remove newlines
instructions = ''.join(instructions.split('\n'))

m = defaultdict(str)

ls = l.split('\n')
h  = len(ls)
w  = len(ls[0])

cur_pos = ()

for i, r in enumerate(ls):
    for j, c in enumerate(r):
        pos = (i, j)
        if c == '#':
            m[(i, j)] = 'edge'
        elif c == 'O':
            m[(i, j)] = 'box'
        elif c == '@':
            cur_pos = pos

def gps_coordinate(pos):
    i, j = pos
    return 100 * i + j

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

for instruction in instructions:
    i, j   = cur_pos
    di, dj = directions[instruction]

    can_move        = True
    last_box_coords = ()

    new_i, new_j = i, j
    while True:
        new_i += di
        new_j += dj
        space = m[(new_i, new_j)]
        if space == '':
            break
        elif space == 'edge':
            can_move = False
            break
        elif space == 'box':
            last_box_coords = (new_i, new_j)
    
    if can_move:
        cur_pos = (i + di, j + dj)
        if cur_pos in m:
            del m[cur_pos] # free up current space after moving affected boxes
        if len(last_box_coords) > 0: # if we moved any boxes
            last_i, last_j = last_box_coords # position of last affected box in current line
            m[(last_i + di, last_j + dj)] = 'box'

s = sum(map(lambda pos: gps_coordinate(pos) if m[pos] == 'box' else 0, m))

print(s)