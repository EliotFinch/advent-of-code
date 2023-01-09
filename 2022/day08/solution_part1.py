import numpy as np

with open('input.txt') as f:
    heights = np.array([
        [int(h) for h in line.strip()] for line in f.readlines()
        ])
    
# Grid dimensions
I, J = heights.shape

# A array of bools indicating whether a tree is visible or not. Initially we
# set all trees to be invisible
visible = np.zeros_like(heights)

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        
        # The outtermost trees are always visisble
        if (i==0) or (i==I-1) or (j==0) or (j==J-1):
            visible[i,j] = 1
        
        else:
            # A tree is visible if along any direction all the heights are 
            # less than the tree height
            for direction in [row[:j], row[j+1:], heights[:i,j], heights[i+1:,j]]:
                if max(direction) < height:
                    visible[i,j] = 1
            
print(np.sum(visible))