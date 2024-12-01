with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

l1 = []
l2 = []
for r in l:
    n1, n2 = map(int, r.split())
    l1.append(n1)
    l2.append(n2)

l1.sort()
l2.sort()

diffs = [abs(l1[i] - l2[i]) for i in range(len(l1))]

print(sum(diffs))