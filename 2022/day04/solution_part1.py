with open('input.txt', 'r') as f:
    input_pairs = [line.strip().split(',') for line in f.readlines()]
        
overlapping_pairs = 0
for i, j in input_pairs:
    
    range_i = [int(s) for s in i.split('-')]
    range_j = [int(s) for s in j.split('-')]
    
    set_i = {s for s in range(range_i[0], range_i[1]+1)}
    set_j = {s for s in range(range_j[0], range_j[1]+1)}
    
    if set_i.issubset(set_j) or set_j.issubset(set_i):
        overlapping_pairs += 1

print(overlapping_pairs)