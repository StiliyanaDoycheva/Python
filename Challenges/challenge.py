list_c = [-14, 7, -9, 2]

max_val = 0
idx_max = 0

for i in range(len(list_c)):
    if list_c[i] > max_val:
        max_val = list_c[i]
        idx_max = i

print(list_c, max_val, idx_max)