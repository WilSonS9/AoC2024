with open('inp.txt', 'r') as f:
    schemas = f.read().split('\n\n')

lock_heights = []
key_heights  = []
for schema in schemas:
    rows    = schema.split('\n')
    height  = [0 for _ in rows[0]]
    is_lock = rows[0][0] == '#'
    if not is_lock:
        rows = rows[::-1]
    for r in rows[1:]:
        for j, c in enumerate(r):
            if c == '#':
                height[j] += 1

    if is_lock:
        lock_heights.append(height)
    else:
        key_heights.append(height)

def is_match(lock_height, key_height):
    for i in range(len(lock_height)):
        if lock_height[i] + key_height[i] <= max_height:
            continue
        return False
    return True

s          = 0
max_height = 5
for lock_height in lock_heights:
    for key_height in key_heights:
        s += is_match(lock_height, key_height)

print(s)