import networkx as nx
from functools import cache

with open('inp.txt', 'r') as f:
    codes = f.read().split('\n')

door_keypad = {(0, 0): '7', (0, 1): '8', (0, 2): '9',
               (1, 0): '4', (1, 1): '5', (1, 2): '6',
               (2, 0): '1', (2, 1): '2', (2, 2): '3',
                            (3, 1): '0', (3, 2): 'A'}

robo_keypad = {             (0, 1): '^', (0, 2): 'A',
               (1, 0): '<', (1, 1): 'v', (1, 2): '>'}

door_inv = {v: k for k, v in door_keypad.items()}
robo_inv = {v: k for k, v in robo_keypad.items()}

h_door = 4
w_door = 3
G_door = nx.Graph()
for i in range(h_door):
    for j in range(w_door):
        if (i, j) == (3, 0):
            continue

        neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
        for neighbour in neighbours:
            i2, j2      = neighbour
            if i2 < 0 or i2 >= h_door or j2 < 0 or j2 >= w_door or (i2, j2) == (3, 0):
                continue
            G_door.add_edge(door_keypad[(i, j)], door_keypad[neighbour])

h_robo = 2
w_robo = 3
G_robo = nx.Graph()
for i in range(h_robo):
    for j in range(w_robo):
        if (i, j) == (0, 0):
            continue

        neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
        for neighbour in neighbours:
            i2, j2      = neighbour
            if i2 < 0 or i2 >= h_robo or j2 < 0 or j2 >= w_robo or (i2, j2) == (0, 0):
                continue
            G_robo.add_edge(robo_keypad[(i, j)], robo_keypad[neighbour])

def get_possible_moves(G, code):
    possible_moves = []
    for i in range(len(code) - 1):
        start = code[i]
        end   = code[i + 1]
        paths = list(nx.all_shortest_paths(G, start, end))
        possible_moves.append(paths)
    return possible_moves

def robo_moves(path, mapping):
    robo_moves = []
    current_i = 0
    while current_i < len(path) - 1:
        start, end = path[current_i], path[current_i + 1]
        current_i += 1

        start_pos = mapping[start]
        end_pos   = mapping[end]

        di, dj = end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]
        if di == 1:
            robo_moves.append('v')
        elif di == -1:
            robo_moves.append('^')
        elif dj == 1:
            robo_moves.append('>')
        elif dj == -1:
            robo_moves.append('<')
    robo_moves.append('A')
    return robo_moves

@cache
def n_moves(start, end, r):
    if r == 25:
        moves   = get_possible_moves(G_robo, f'{start}{end}')
        mapping = robo_inv
        min_cost = 1e100
        for moveset in moves[0]:
            robot_moves = robo_moves(moveset, mapping)
            min_cost = min(len(robot_moves), min_cost)
        return min_cost
    if r == 0:
        moves   = get_possible_moves(G_door, f'{start}{end}')
        mapping = door_inv
    else:
        moves   = get_possible_moves(G_robo, f'{start}{end}')
        mapping = robo_inv

    min_cost = 1e100

    for moveset in moves[0]:
        robot_moves = robo_moves(moveset, mapping)
        moves = 0
        ends   = robot_moves
        starts = 'A' + ''.join(robot_moves[:-1])
        for i in range(len(starts)):
            start = starts[i]
            end   = ends[i]
            cost  = n_moves(start, end, r + 1)
            moves += cost
        min_cost = min(moves, min_cost)
    return min_cost

s_complex = 0
for code in codes:
    new_code = 'A' + code
    s = 0
    for i in range(len(code)):
        start = new_code[i]
        end   = new_code[i + 1]
        s += n_moves(start, end, 0)
    s_complex += s * int(code[:-1])

print(s_complex)