import networkx as nx
from itertools import product

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

def robo_moves(path, mapping):
    robo_moves = []
    for subpath in path:
        current_i = 0
        while current_i < len(subpath) - 1:
            start, end = subpath[current_i], subpath[current_i + 1]
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
    starts = 'A' + code[:-1]
    possible_moves = []
    for i in range(len(code)):
        start = starts[i]
        end   = code[i]
        paths = list(nx.all_shortest_paths(G, start, end))
        possible_moves.append(paths)
    return possible_moves

def get_robo_paths(total_paths, mapping):
    robo_paths = []
    for path in total_paths:
        robo_path = ''.join(mapping(path))
        robo_paths.append(robo_path)
    return robo_paths

def get_possible_paths(G, codes, mapping):
    robo2_paths = []
    min_length  = 1e100
    for code in codes:
        total_moves = get_possible_moves(G, code)
        total_paths = list(product(*total_moves))

        robo1_paths = get_robo_paths(total_paths, lambda path: robo_moves(path, mapping))
        path_lengths = len(robo1_paths[0])
        if path_lengths < min_length:
            robo2_paths = robo1_paths
        elif path_lengths == min_length:
            robo2_paths += robo1_paths
        min_length = min(path_lengths, min_length)
    return robo2_paths

s = 0
for code in codes:
    robo1_moves = get_possible_paths(G_door, [code], door_inv)
    robo2_moves = get_possible_paths(G_robo, robo1_moves, robo_inv)
    robo3_moves = get_possible_paths(G_robo, robo2_moves, robo_inv)
    min_length  = len(robo3_moves[0])
    s += min_length * int(code[:-1])

print(s)