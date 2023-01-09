import numpy as np

with open('input.txt') as f:
    hmap_lines = [line.strip() for line in f.readlines()]
    
for i, line in enumerate(hmap_lines):
    for j, letter in enumerate(line):
        if letter == 'S':
            start = (j, i)
        elif letter == 'E':
            end = (j, i)

for i, line in enumerate(hmap_lines):
    hmap_lines[i] = line.replace('S', 'a').replace('E', 'z')
hmap = np.array([[ord(c) for c in line] for line in hmap_lines])

map_shape = hmap.shape
    
paths = [[start]]
visited = [start]

while end not in visited:
    
    # A list of new paths with all possible steps from the current paths
    new_paths = []
    
    for path in paths:
        
        current_x, current_y = path[-1]
        current_height = hmap[current_y, current_x]
        
        proposed_steps = [
            (current_x, current_y+1), 
            (current_x+1, current_y),
            (current_x, current_y-1),
            (current_x-1, current_y)
            ]
        
        for proposed_step in proposed_steps:
            
            px, py = proposed_step
            
            # Check the proposed step is on the map
            if ((px >= 0) & (px < map_shape[1]) & (py >= 0) & (py < map_shape[0])):
                
                proposed_height = hmap[py, px]
                
                # We don't want to visit previously visited steps, and we
                # can't increase height more than 1
                if ((proposed_step in visited) | (proposed_height - current_height > 1)):
                    pass
                else:
                    new_paths.append(path + [proposed_step])
                    visited.append(proposed_step)
            
    paths = new_paths
    
for path in paths:
    if end in path:
        print(len(path)-1)