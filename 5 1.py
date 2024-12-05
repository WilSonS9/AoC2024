from collections import defaultdict

with open('inp.txt', 'r') as f:
    l1, l2 = f.read().split('\n\n')

rules = defaultdict(list)
for r in l1.split('\n'):
    n1, n2 = map(int, r.split('|'))
    rules[n1].append(n2)

sequences = []
for r in l2.split('\n'):
    sequences.append(list(map(int, r.split(','))))

def control_sequence(sequence, rules):
    for i, n1 in enumerate(sequence):
        for n2 in rules[n1]:
            if n2 in sequence and sequence.index(n2) < i:
                return False
    return True
            
s = 0
for sequence in sequences:
    valid = control_sequence(sequence, rules)
    if valid:
        s += sequence[len(sequence)//2]

print(s)