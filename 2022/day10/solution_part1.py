with open('input.txt') as f:
    program = [line.split() for line in f.readlines()]

def check_score(X, cycle):
    return X*cycle

# Value of the X register
X = 1

# The cycle we are currently executing
cycle = 1

# List to store scores of interest
score_list = []

for instruction in program:
    
    if instruction[0] == 'noop':
        
        # Proceed to the next cycle
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            score_list.append(check_score(X,cycle))
        
    elif instruction[0] == 'addx':
        
        # Proceed to the next cycle
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            score_list.append(check_score(X,cycle))
        
        # Proceed to the next cycle
        cycle += 1
        
        # The instruction finishes executing, adjusting the X register
        X += int(instruction[1])
        
        if cycle in [20, 60, 100, 140, 180, 220]:
            score_list.append(check_score(X,cycle))

print(sum(score_list))