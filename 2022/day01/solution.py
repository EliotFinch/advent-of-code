with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# List to store total Calories associated with each elf
total_Calories = [0]

# Elf counter
i = 0

for line in lines:
    
    if line == '':
        # Increase elf counter and add a new entry to the total_Calories list
        i += 1
        total_Calories.append(0)
        
    else:
        Calories = int(line)
        total_Calories[i] += Calories
        
print(max(total_Calories))
print(sum(sorted(total_Calories)[-3:]))