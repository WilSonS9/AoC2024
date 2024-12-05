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

def corrected_sequence(sequence, rules):
    '''create a new list with swapped places of the first incorrectly ordered pair. use this function repeatedly.
    
    returns list `new_sequence`, bool `valid`'''

    new_sequence = sequence[:]
    for i, n1 in enumerate(sequence):
        for n2 in rules[n1]:
            if n2 in sequence:
                j = sequence.index(n2)
                if j < i:
                    new_sequence[i] = sequence[j]
                    new_sequence[j] = sequence[i]
                    return new_sequence, False
    return new_sequence, True


invalid_sequences = []
for sequence in sequences:
    valid = control_sequence(sequence, rules)
    if not valid:
        invalid_sequences.append(sequence)

s = 0
for sequence in invalid_sequences:
    valid = False
    while not valid:
        sequence, valid = corrected_sequence(sequence, rules)
    s += sequence[len(sequence)//2]

print(s)