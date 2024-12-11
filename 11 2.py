from functools import cache

with open('inp.txt', 'r') as f:
    ns = tuple(map(int, f.read().split(' ')))

@cache
def n_stones(iterations_left, n):
    if iterations_left == 0:
        return 1
    
    if n == 0:
        return n_stones(iterations_left - 1, 1)

    n_string = str(n)
    n_digits = len(n_string)
    if n_digits % 2 == 0:
        n1, n2 = map(int, [n_string[:n_digits//2], n_string[n_digits//2:]])
        return n_stones(iterations_left - 1, n1) + n_stones(iterations_left - 1, n2)

    return n_stones(iterations_left - 1, 2024 * n)

n_iterations = 75
s = sum(map(lambda n: n_stones(n_iterations, n), ns))
print(s)