import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = 71
w = 71

start = (0, 0)
end   = (h - 1, w - 1)

n_bytes = 1024

fallen_bytes = set()
for r in l[:n_bytes]:
    i, j = map(int, r.split(','))
    fallen_bytes.add((i, j))

G = nx.Graph()
for i in range(h):
    for j in range(w):
        coord = (i, j)
        if not coord in fallen_bytes:
            neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            for neighbour in neighbours:
                i2, j2 = neighbour
                if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                    continue
                if not neighbour in fallen_bytes:
                    G.add_edge(coord, neighbour)

path_length = nx.shortest_path_length(G, source=start, target=end)          
print(path_length)      