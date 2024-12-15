from collections import defaultdict

with open('inp.txt', 'r') as f:
    l, instructions = f.read().split('\n\n')

# remove newlines
instructions = ''.join(instructions.split('\n'))

# expand map
new_l = []
for line in l.split('\n'):
    new_line = line.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]')
    new_l.append(new_line)

ls = new_l

m = defaultdict(str)

h  = len(ls)
w  = len(ls[0])

cur_pos = ()

for i, r in enumerate(ls):
    for j, c in enumerate(r):
        pos = (i, j)
        if c == '#':
            m[(i, j)] = 'edge'
        elif c == '[':
            m[(i, j)] = '['
        elif c == ']':
            m[(i, j)] = ']'
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

    pushing_coords = [(i, j)] # frontier of our pushing coordinates
    old_boxes      = []
    new_boxes      = []
    while True:
        new_pushing_coords = []

        ready_to_move = True

        for (ip, jp) in pushing_coords:
            new_i = ip + di
            new_j = jp + dj
            space = m[(new_i, new_j)]
            if space == '':
                continue
            elif space == 'edge':
                can_move      = False
                ready_to_move = False # cannot move, edge has been reached
                break
            elif space == '[':
                box_coords         = [(new_i, new_j), (new_i, new_j + 1)]
                old_boxes          += box_coords
                if instruction == '>':
                    new_pushing_coords += [(new_i, new_j + 1)]
                else:
                    new_pushing_coords += box_coords
                new_boxes          += [(new_i + di, new_j + dj, '['), (new_i + di, new_j + dj + 1, ']')]
                ready_to_move      = False # need to continue looking at pushes
            elif space == ']':
                box_coords         = [(new_i, new_j - 1), (new_i, new_j)]
                old_boxes          += box_coords
                if instruction == '<':
                    new_pushing_coords += [(new_i, new_j - 1)]
                else:
                    new_pushing_coords += box_coords
                new_boxes          += [(new_i + di, new_j + dj - 1, '['), (new_i + di, new_j + dj, ']')]
                ready_to_move      = False # need to continue looking at pushes
        
        pushing_coords = new_pushing_coords[:]
        
        if ready_to_move:
            break
    
    if can_move:
        cur_pos = (i + di, j + dj)
        for pos in list(set(old_boxes)): # remove duplicates in case one box has both sides pushing on another box
            del m[pos]
        for (i, j, c) in new_boxes:
            m[(i, j)] = c

s = sum(map(lambda pos: gps_coordinate(pos) if m[pos] == '[' else 0, m))

print(s)