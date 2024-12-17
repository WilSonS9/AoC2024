from z3 import *

# program is simply a loop that repeats until register A = 0, adding an output at the end of each iteration
# solution: add one constraint for each iteration of the loop stating that the output of the loop must match the given instruction
# and register A should be 0 after 16 iterations of the loop (length of instructions)

with open('inp.txt', 'r') as f:
    r_s, i_s = f.read().split('\n\n')

registers = {}
for r in r_s.split('\n'):
    bs             = r.split(': ')
    value          = int(bs[1])
    reg            = bs[0].split(' ')[1]
    registers[reg] = value

instructions = [int(code) for code in i_s.split(' ')[1].split(',')]

opt = Optimize()
s = BitVec('s', 64)
A, B, C = s, registers['B'], registers['C']
for x in instructions:
    # decompiled program (some of the instructions vary depending on input)
    B = A % 8
    B = B ^ 5
    C = A / (1 << B) # A / B truncated
    A = A / (1 << 3)
    B = B ^ C
    B = B ^ 6
    opt.add((B % 8) == x)

opt.add(A == 0)
opt.minimize(s) # we want the smallest value that outputs the program itself
opt.check() # solve (takes a while)
print(opt.model().eval(s))