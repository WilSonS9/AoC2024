import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

G = nx.Graph()
for r in l:
    v1, v2 = r.split('-')
    G.add_edge(v1, v2)

clique   = max(nx.find_cliques(G), key=lambda c: len(c))
password = ','.join(sorted(clique))

print(password)