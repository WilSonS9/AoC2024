with open('inp.txt', 'r') as f:
    ns = list(map(int, f.read().split(' ')))

for i in range(25):
    new_ns = []
    for n in ns:
        if n == 0:
            new_ns.append(1)
        else:
            n_string = str(n)
            n_digits = len(n_string)
            if n_digits % 2 == 0:
                n1, n2 = map(int, [n_string[:n_digits//2], n_string[n_digits//2:]])
                new_ns.append(n1)
                new_ns.append(n2)
            else:
                new_ns.append(2024 * n)
    ns = new_ns[:]

print(len(ns))