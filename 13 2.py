import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

s = 0

for block in l:
    r1, r2, r3 = block.split('\n')
    x1, y1 = map(lambda s: int(s[2:]), r1.split(': ')[1].split(', '))
    x2, y2 = map(lambda s: int(s[2:]), r2.split(': ')[1].split(', '))
    x, y   = map(lambda s: int(s[2:]) + 10000000000000, r3.split(': ')[1].split(', '))

    A = np.matrix([[x1, x2], [y1, y2]])
    b = np.array([x, y])
    x = np.linalg.solve(A, b)

    if all(map(lambda n: round(n, 2).is_integer(), x)):
        s += int(x.round() @ [3, 1])
    
print(s)