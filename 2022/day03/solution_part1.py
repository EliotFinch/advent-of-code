with open('input.txt', 'r') as f:
    rucksacks = [line.strip() for line in f.readlines()]

priority_sum = 0
for r in rucksacks:
    
    split_index = int(len(r)/2)
    c1, c2 = r[:split_index], r[split_index:]
    
    common_item = (set(c1).intersection(set(c2))).pop()
    
    if common_item.islower():
        priority_sum += ord(common_item) - 96
    else:
        priority_sum += ord(common_item) - 38
        
print(priority_sum)