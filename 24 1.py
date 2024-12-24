with open('inp.txt', 'r') as f:
    l1, l2 = f.read().split('\n\n')

state  = {}
z_vars = set()

for r in l1.split('\n'):
    var, val   = r.split(': ')
    state[var] = int(val)

assignment_rows = l2.split('\n')
while len(assignment_rows) > 0:
    new_assignment_rows = []
    for r in assignment_rows:
        inp, outp = r.split(' -> ')
        if outp[0] == 'z':
            z_vars.add(outp)
        
        v1, op, v2 = inp.split(' ')
        if not v1 in state.keys() or not v2 in state.keys():
            new_assignment_rows.append(r)
            continue
        if op == 'AND':
            state[outp] = state[v1] and state[v2]
        elif op == 'OR':
            state[outp] = state[v1] or state[v2]
        elif op == 'XOR':
            state[outp] = state[v1] ^ state[v2]
    assignment_rows = new_assignment_rows

s = ''
for z in sorted(list(z_vars)):
    s = str(state[z]) + s

s = int(s, 2)

print(s)