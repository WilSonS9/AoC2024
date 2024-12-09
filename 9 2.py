with open('inp.txt', 'r') as f:
    l = f.read()

blocks      = []
current_pos = 0
max_index   = 0

for i, c in enumerate(l):
    size = int(c)
    if i % 2 == 0:
        f_start = current_pos
        f_end   = current_pos + size - 1
        blocks.append((i // 2, (f_start, f_end)))
        current_pos = f_end + 1
        max_index   = i // 2
    else:
        current_pos += size

def find_free_space(blocks, lim, end):
    prev_f_end = -1
    for i, block in enumerate(blocks):
        _, (f_start, f_end) = block
        if f_start > end:
            break
        if f_start - prev_f_end > 1:
            free_space_start = prev_f_end + 1
            free_space_end   = f_start - 1

            size = free_space_end - free_space_start + 1
            if size >= lim:
                return True, i, (free_space_start, free_space_end)
        
        prev_f_end = f_end
    return False, -1, ()

length = len(blocks)

while max_index > 0:
    for j in range(length - 1, 0, -1):
        i, (f_start, f_end) = blocks[j]
        if i == max_index:
            largest_unvisited_index = j
            break

    file_size = f_end - f_start + 1

    exists_free, block_number, block = find_free_space(blocks, file_size, f_end)
    if exists_free:
        block_start, block_end = block
        new_block              = (i, (block_start, block_start + file_size - 1))

        blocks.pop(largest_unvisited_index)
        blocks = blocks[:block_number] + [new_block] + blocks[block_number:]
    
    max_index -= 1

s       = 0
cur_pos = 0
for block in blocks:
    i, (f_start, f_end) = block
    cur_pos             = f_start
    while cur_pos <= f_end:
        s       += i * cur_pos
        cur_pos += 1

print(s)