from collections import defaultdict
from functools import cache

with open('inp.txt', 'r') as f:
    tow_s, pat_s = f.read().split('\n\n')

towels    = tow_s.split(', ')
patterns  = pat_s.split('\n')

towel_letters = defaultdict(list) # organize towels by first letter to limit number of options somewhat
for towel in towels:
    towel_letters[towel[0]].append(towel)

@cache
def n_ways(pattern):
    global towel_letters
    if len(pattern) == 0: # base case
        return 1

    n            = 0
    first_letter = pattern[0]
    for towel in towel_letters[first_letter]:
        matches_start = True
        if len(towel) > len(pattern):
            continue
        for i, letter in enumerate(towel):
            if pattern[i] != letter:
                matches_start = False
                break
        if matches_start:
            n += n_ways(pattern[len(towel):])
    return n

s = 0
for pattern in patterns:
    s += n_ways(pattern)

print(s)