with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]
    
    # Convert entries to lists of the form [(x1,y1),(x2,y2)]
    data = []
    for i, line in enumerate(lines):
        coord_pair = []
        for coords in line.split(' -> '):
            coords = [int(coord) for coord in coords.split(',')]
            coord_pair.append(coords)
        data.append(coord_pair)
        
# If we only want to consider only horizontal and vertical lines
data_reduced = []
for xy1, xy2 in data:
    x1, y1 = xy1
    if (x1 in xy2) | (y1 in xy2):
        data_reduced.append([xy1, xy2])
        
# Get the extent of the coordinates
max_x = 0
max_y = 0
for (x1, y1), (x2, y2) in data:
    max_x_proposal = max([x1, x2])
    max_y_proposal = max([y1, y2])
    if max_x_proposal > max_x:
        max_x = max_x_proposal
    if max_y_proposal > max_y:
        max_y = max_y_proposal
        
# Create an empty grid of zeros
grid = [(max_x+1)*[0] for _ in range(max_y+1)]

# Add the line counts to the grid
for (x1, y1), (x2, y2) in data:
    
    x_min, x_max = min([x1, x2]), max([x1,x2])
    y_min, y_max = min([y1, y2]), max([y1,y2])
    
    if x1 == x2:
        for i in range(y_min,y_max+1):
            grid[i][x1] += 1
    elif y1 == y2:
        for i in range(x_min,x_max+1):
            grid[y1][i] += 1
    else:
        x_values = range(x_min, x_max+1)
        if x1 > x2:
            x_values = reversed(x_values)
        y_values = range(y_min, y_max+1)
        if y1 > y2:
            y_values = reversed(y_values)
        for i, j in zip(x_values, y_values):
            grid[j][i] += 1
            
# Count points with overlapping lines
out = 0
for row in grid:
    for entry in row:
        if entry > 1:
            out += 1
            
print(out)