with open('inp.txt', 'r') as f:
    r_s, i_s = f.read().split('\n\n')

registers = {}
for r in r_s.split('\n'):
    bs             = r.split(': ')
    value          = int(bs[1])
    reg            = bs[0].split(' ')[1]
    registers[reg] = value

instructions   = [int(code) for code in i_s.split(' ')[1].split(',')]
n_instructions = len(instructions)

registers['i'] = 0
registers['o'] = []

def combo(registers, operand):
    op_reg = {4: 'A', 5: 'B', 6: 'C'}
    if operand <= 3:
        return operand
    elif operand <= 6:
        return registers[op_reg[operand]]
    registers['i'] += 2

def adv(registers, operand):
    num = registers['A']
    den = 2 ** combo(registers, operand)
    res = int(num / den)
    registers['A'] = res
    registers['i'] += 2

def bxl(registers, operand):
    registers['B'] = registers['B'] ^ operand
    registers['i'] += 2

def bst(registers, operand):
    registers['B'] = combo(registers, operand) % 8
    registers['i'] += 2

def jnz(registers, operand):
    if registers['A'] == 0:
        registers['i'] += 2
        return
    registers['i'] = operand

def bxc(registers, _):
    registers['B'] = registers['B'] ^ registers['C']
    registers['i'] += 2

def out(registers, operand):
    registers['o'].append(combo(registers, operand) % 8)
    registers['i'] += 2

def bdv(registers, operand):
    num = registers['A']
    den = 2 ** combo(registers, operand)
    res = int(num / den)
    registers['B'] = res
    registers['i'] += 2

def cdv(registers, operand):
    num = registers['A']
    den = 2 ** combo(registers, operand)
    res = int(num / den)
    registers['C'] = res
    registers['i'] += 2

opcode_functions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

while registers['i'] < n_instructions - 1:
    i               = registers['i']
    opcode, operand = instructions[i], instructions[i + 1]

    func = opcode_functions[opcode]
    func(registers, operand)

print(','.join(map(str, registers['o'])))