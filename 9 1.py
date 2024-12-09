with open('inp.txt', 'r') as f:
    l = f.read()

blocks      = []
current_pos = 0
for i, c in enumerate(l):
    size = int(c)
    if i % 2 == 0:
        f_start = current_pos
        f_end   = current_pos + size - 1
        blocks.append((i // 2, (f_start, f_end)))
        current_pos = f_end + 1
    else:
        current_pos += size

def find_free_space(blocks):
    prev_f_end = -1
    for i, block in enumerate(blocks):
        _, (f_start, f_end) = block
        if f_start - prev_f_end > 1:
            free_space_start = prev_f_end + 1
            free_space_end   = f_start - 1
            return True, i, (free_space_start, free_space_end)
        
        prev_f_end = f_end
    return False, -1, ()

while True:
    exists_free, block_number, block = find_free_space(blocks)
    if not exists_free:
        break
    block_start, block_end = block
    i, (f_start, f_end) = blocks[-1]

    blocks = blocks[:-1]

    space_size = block_end - block_start + 1
    file_size  = f_end - f_start + 1
    if file_size <= space_size:
        new_block = (i, (block_start, block_start + file_size - 1))
        blocks = blocks[:block_number] + [new_block] + blocks[block_number:]
    else:
        new_block       = (i, (block_start, block_start + space_size - 1))
        remaining_block = (i, (f_start, f_start + file_size - space_size - 1))
        blocks = blocks[:block_number] + [new_block] + blocks[block_number:] + [remaining_block]

s       = 0
cur_pos = 0
for block in blocks:
    i, (f_start, f_end) = block
    while cur_pos <= f_end:
        s       += i * cur_pos
        cur_pos += 1

print(s)