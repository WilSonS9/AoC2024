with open('inp.txt', 'r') as f:
    l1, l2 = f.read().split('\n\n')

n_vars = {'x': set(), 'y': set(), 'z': set()}

for r in l1.split('\n'):
    var, val   = r.split(': ')
    first_char = var[0]
    if first_char in 'xy':
        n_vars[first_char].add(var)

wrong_registers = set()

xyadd   = set()
xycarry = set()
carries = set()
ands    = set()
outs    = set()

carries_rows = set() # rows computing carry variables
outs_rows    = set() # rows computing outputs

assignment_rows = l2.split('\n')
for r in assignment_rows:
    inp, outp  = r.split(' -> ')

    v1, op, v2 = inp.split(' ')

    if v1[0] in 'xy' or v2[0] in 'xy':
        if op == 'AND':
            # special case
            if v1 == 'x00' and v2 == 'y00':
                continue
            xycarry.add(outp)
        elif op == 'XOR':
            if outp[0] == 'z' and outp != 'z00':
                wrong_registers.add(outp)
            # special case
            if outp == 'z00':
                continue
            xyadd.add(outp)
    else:
        if op == 'AND':
            ands.add(outp)
        elif op == 'OR':
            carries.add(outp)
            carries_rows.add((v1, v2, outp))
        elif op == 'XOR':
            # XOR operations should only output to z variables
            if outp[0] != 'z':
                wrong_registers.add(outp)
            outs.add(outp)
            outs_rows.add((v1, v2, outp))

    # z variables should only appear as results of an XOR operation
    # except for the final variable which should be the result of an OR operation
    if outp[0] == 'z':
        n_vars['z'].add(outp)
        if op != 'XOR' and not (outp == 'z45' and op == 'OR'):
            wrong_registers.add(outp)

# xycarry variables should appear in some carry row (except for the first xycarry result from x00 and y00)
for carry in xycarry:
    valid = False
    for (v1, v2, _) in carries_rows:
        if carry == v1 or carry == v2:
            valid = True
            break
    if not valid:
        wrong_registers.add(carry)

# xyadd variables should appear in some output row (except for the first xyadd result z00)
for add in xyadd:
    valid = False
    for (v1, v2, _) in outs_rows:
        if add == v1 or add == v2:
            valid = True
            break
    if not valid:
        wrong_registers.add(add)

print(','.join(sorted(list(wrong_registers))))