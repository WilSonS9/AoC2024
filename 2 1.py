with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def is_correct(ns):
    if ns[-1] == ns[0]:
        # either the jump at the end is too big or we change sign too often for the list to be valid
        return 0

    dir = sgn(ns[-1] - ns[0])

    cur = ns[0]
    for n in ns[1:]:
        delta = n - cur
        if abs(delta) >= 1 and abs(delta) <= 3 and sgn(delta) == dir:
            cur = n
        else:
            return 0
    return 1

def sgn(x):
    return x / abs(x)

s = 0

for r in l:
    ns = list(map(int, r.split()))
    s += is_correct(ns)

print(s)