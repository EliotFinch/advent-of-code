with open('input.txt') as f:
    input_data = [line.rstrip() for line in f]

# Initialize the stacks
stacks = {n: [] for n in range(1,10)}
for line in input_data:
    
    if line[:3] == ' 1 ':
        break
    
    for i, char in enumerate(line):
        if char.isalnum():
            stacks[(i//4)+1].append(char)
            
# Re-arrange stacks
for line in input_data:
    if line[:4] == 'move':
        _, number_to_move, _, stack1, _, stack2 = line.split()
        number_to_move, stack1, stack2 = int(number_to_move), int(stack1), int(stack2)
        
        # Move one crate at a time
        # stacks[stack2] = stacks[stack1][:number_to_move][::-1] + stacks[stack2]
        
        # Move multiple crates at once
        stacks[stack2] = stacks[stack1][:number_to_move] + stacks[stack2]
        stacks[stack1] = stacks[stack1][number_to_move:]
    
print(''.join([stack[0] for stack in stacks.values()]))