with open('input.txt') as f:
    movements = [line.split() for line in f.readlines()]

# Store the [x,y] position of each rope segment in a dictionary
rope_length = 10
positions = {i: [0,0] for i in range(rope_length)}

# Keep track of all the places the end of the rope visits
tail_history = [[0,0]]

def update_position(pos_1, pos_2):
    """
    Given rope segment positions pos_1 and pos_2, update pos_2 based on pos_1
    (i.e. if pos_1 = [2,0] and pos_2 = [0,0], the function updates pos_2 to
    pos_2 = [1,0]).
    """
    
    # Extract coordinates
    x1, y1 = pos_1
    x2, y2 = pos_2
    
    dx = x2 - x1
    dy = y2 - y1
    
    # The case where the position doesn't change
    distance_squared = (dx)**2 + (dy)**2
    if distance_squared in [0,1,2]:
        pass
    
    # All posibilties for movement
    else:
        
        if (dx == 2) and (dy == 2):
            pos_2 = [x1+1, y1+1]
            
        elif (dx == 2) and (dy == -2):
            pos_2 = [x1+1, y1-1]
            
        elif (dx == -2) and (dy == -2):
            pos_2 = [x1-1, y1-1]
            
        elif (dx == -2) and (dy == 2):
            pos_2 = [x1-1, y1+1]
        
        elif dy == 2:
            pos_2 = [x1, y1+1]
        
        elif dx == 2:
            pos_2 = [x1+1, y1]
        
        elif dy == -2:
            pos_2 = [x1, y1-1]
            
        elif dx == -2:
            pos_2 = [x1-1, y1]
    
    return pos_2

# Go through the movements
for direction, N in movements:
    
    for i in range(int(N)):
        
        # Update head position
        if direction == 'L':
            positions[0][0] -= 1
        if direction == 'R':
            positions[0][0] += 1
        if direction == 'U':
            positions[0][1] += 1
        if direction == 'D':
            positions[0][1] -= 1
        
        # Update all other positions based on how the one ahead moved
        for j in range(1, rope_length):
            positions[j] = update_position(positions[j-1], positions[j])
        
        # Record the tail position if it has visited somewhere new
        tail_position = positions[rope_length-1]
        if tail_position not in tail_history:
            tail_history.append(tail_position)

print(len(tail_history))