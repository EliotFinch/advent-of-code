with open('input.txt') as f:
    program = [line.split() for line in f.readlines()]

# We build the CRT screen up as a list (a pixel is always drawn at the start)
CRT = '#'

# Location of the middle of the sprite
X = 1

# The cycle we are currently executing. This also determines the pixel that is 
# drawn.
cycle = 1

def draw(CRT, X, cycle):
    
    if (cycle-1)%40 in [X-1,X,X+1]:
        CRT += '#'
    else:
        CRT += ' '
        
    return CRT

for instruction in program:
    
    if instruction[0] == 'noop':
        
        cycle += 1
        CRT = draw(CRT, X, cycle)
        
    elif instruction[0] == 'addx':
        
        cycle += 1
        CRT = draw(CRT, X, cycle)
        
        cycle += 1
        X += int(instruction[1])
        CRT = draw(CRT, X, cycle)

for i in range(len(CRT)//40):
    print(CRT[i*40:(i+1)*40])