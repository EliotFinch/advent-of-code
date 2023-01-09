with open('input.txt', 'r') as f:
    rucksacks = [line.strip() for line in f.readlines()]
    
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

priority_sum = 0
for r1, r2, r3 in groups:
    
    common_item = ((set(r1).intersection(set(r2))).intersection(set(r3))).pop()
    
    if common_item.islower():
        priority_sum += ord(common_item) - 96
    else:
        priority_sum += ord(common_item) - 38
        
print(priority_sum)