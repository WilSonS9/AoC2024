import itertools

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

m = [[c for c in r] for r in l]

def starts_x_mas(m, i, j):

    new_indices = [(i + d_i, j + d_j) for d_i, d_j in itertools.product([1, -1], [1, -1])] # all corners of our x-mas

    i_dr, j_dr = new_indices[0]
    i_dl, j_dl = new_indices[1]
    i_ur, j_ur = new_indices[2]
    i_ul, j_ul = new_indices[3]

    c_dr = m[i_dr][j_dr]
    c_dl = m[i_dl][j_dl]
    c_ur = m[i_ur][j_ur]
    c_ul = m[i_ul][j_ul]
    
    # 4 possible x-mas configurations, check each one
    if c_dr == 'M':
        if c_ur == 'M':
            return int(c_ul == 'S' and c_dl == 'S')
        elif c_dl == 'M':
            return int(c_ul == 'S' and c_ur == 'S')
    elif c_dr == 'S':
        if c_ur == 'S':
            return int(c_ul == 'M' and c_dl == 'M')
        elif c_dl == 'S':
            return int(c_ul == 'M' and c_ur == 'M')

    return 0

total_s = 0

# no need to search along the edges since an x-mas is impossible
for i, r in enumerate(l[1:-1]):
    for j, c in enumerate(r[1:-1]):
        if c == 'A':
            total_s += starts_x_mas(m, i + 1, j + 1) # +1 on indices since i, j in this case start at 0 within the edge

print(total_s)