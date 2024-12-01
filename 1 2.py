from collections import defaultdict

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

l1 = []
l2 = []
for r in l:
    n1, n2 = map(int, r.split())
    l1.append(n1)
    l2.append(n2)

n_right_occurences = defaultdict(int)
for n in l2:
    n_right_occurences[n] += 1

s = sum(map(lambda n: n * n_right_occurences[n], l1))

print(s)