import numpy as np

with open('input.txt') as f:
    lines = [
        [tuple(int(c) for c in xy.split(',')) for xy in line.strip().split('->')] 
        for line in f.readlines()
        ]

# Create grid

xcoords = [xy[0] for line in lines for xy in line]
xmin, xmax = 0, 1000 # min(xcoords), max(xcoords)

ycoords = [xy[1] for line in lines for xy in line]
ymin, ymax = 0, max(ycoords) + 2

grid = np.ones((ymax-ymin+1, xmax-xmin+1))

# Draw lines

for line in lines:
    for i in range(len(line) - 1):
        x0, y0 = line[i]
        x1, y1 = line[i+1]
        grid[
            min([y0,y1])-ymin:max([y0,y1])-ymin+1, 
            min([x0,x1])-xmin:max([x0,x1])-xmin+1
            ] = 0
        
grid[ymax:ymax+1:,:] = 0
        
# Pour sand

at_rest = 0
xi, yi = 500-xmin, 0-ymin

while grid[0-ymin,500-xmin]:
    
    if grid[yi+1,xi]:
        yi += 1
    elif grid[yi+1,xi-1]:
        yi += 1
        xi -= 1
    elif grid[yi+1,xi+1]:
        yi += 1
        xi += 1
    else:
        grid[yi,xi] = 0
        at_rest += 1
        xi, yi = 500-xmin, 0-ymin
        
print(at_rest)