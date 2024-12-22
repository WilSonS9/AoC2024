from collections import defaultdict

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

sequence_profits = defaultdict(int)
n_iters   = 2000
for n in ns:
    cur_sequence   = []
    prev_price     = n % 10
    prev_sequences = set()
    for i in range(n_iters):
        n     = next_secret(n)
        price = n % 10
        delta = price - prev_price
        cur_sequence.append(delta)

        if len(cur_sequence) > 4:
            cur_sequence = cur_sequence[1:]

        if i >= 3:
            cur_tuple = tuple(cur_sequence)
            if not cur_tuple in prev_sequences:
                sequence_profits[cur_tuple] += price
                prev_sequences.add(cur_tuple)

        prev_price = price

max_profit = max(sequence_profits.values())
print(max_profit)