with open('inp.txt', 'r') as f:
    ns = map(int, f.read().split('\n'))

def mix(secret, val):
    return secret ^ val

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    n = secret
    n2 = prune(mix(n, 64 * n))
    n3 = prune(mix(n2, n2 // 32))
    n4 = prune(mix(n3, 2048 * n3))
    return n4

s       = 0
n_iters = 2000
for n in ns:
    for _ in range(n_iters):
        n = next_secret(n)
    s += n

print(s)