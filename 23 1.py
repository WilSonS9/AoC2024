import networkx as nx

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

G = nx.Graph()
for r in l:
    v1, v2 = r.split('-')
    G.add_edge(v1, v2)

cliques = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]
s       = sum(map(lambda triple: triple[0][0] == 't' or triple[1][0] == 't' or triple[2][0] == 't', cliques))

print(s)