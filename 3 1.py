import re

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

s = 0
for r in l:
    matches = re.findall(r'mul\(\d+,\d+\)', r)
    for match in matches:
        s1, s2 = match.split(',')
        n1 = int(s1[4:])
        n2 = int(s2[:-1])
        s += n1 * n2

print(s)