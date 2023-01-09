with open('input.txt') as f:
    movements = [line.split() for line in f.readlines()]

# Initial positions
H_pos = [0,0]
T_pos = [0,0]

# Keep track of tail position history
T_hist = [[0,0]]
unique_T_hist = [[0,0]]

def update_pos(direction, H_pos, T_pos):
    
    Hx, Hy = H_pos
    Tx, Ty = T_pos
    
    # Update head position
    if direction == 'L':
        Hx -= 1
    if direction == 'R':
        Hx += 1
    if direction == 'U':
        Hy += 1
    if direction == 'D':
        Hy -= 1
    H_pos = [Hx,Hy]
    
    # Update tail position
    dx = Tx - Hx
    dy = Ty - Hy
    
    distance_squared = (dx)**2 + (dy)**2
    
    if distance_squared in [1,2]:
        pass
    
    else:
        
        if dy == 2:
            T_pos = [Hx, Hy+1]
        
        if dx == 2:
            T_pos = [Hx+1, Hy]
        
        if dy == -2:
            T_pos = [Hx, Hy-1]
            
        if dx == -2:
            T_pos = [Hx-1, Hy]
    
    return H_pos, T_pos

for direction, N in movements:
    for i in range(int(N)):
        H_pos, T_pos = update_pos(direction, H_pos, T_pos)
        T_hist.append(T_pos)
        if T_pos not in unique_T_hist:
            unique_T_hist.append(T_pos)

print(len(unique_T_hist))