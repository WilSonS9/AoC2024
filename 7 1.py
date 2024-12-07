import itertools

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def try_combination(n1, ns, ops):
    val = ns[0]
    for i, op in enumerate(ops):
        new_n = ns[i + 1]
        if op == '+':
            val += new_n
        elif op == '*':
            val *= new_n
    
    return val == n1, val

operation_permutations = {}
completed_n_ops        = set()
n_possible             = 0
s                      = 0
operations             = ['+', '*']

for i, r in enumerate(l):
    n1_s, ns_s = r.split(': ')
    n1    = int(n1_s)
    ns    = list(map(int, ns_s.split(' ')))
    n_ops = len(ns) - 1

    if not n_ops in completed_n_ops:
        operation_permutations[n_ops] = list(itertools.product(operations, repeat=n_ops))
        completed_n_ops.add(n_ops)
    
    possible_ops = operation_permutations[n_ops]
    for ops in possible_ops:
        suc, val = try_combination(n1, ns, ops)
        if suc:
            n_possible += 1
            s += val
            break

print(s)