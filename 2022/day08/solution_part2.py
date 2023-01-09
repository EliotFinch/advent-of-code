import numpy as np

with open('input.txt') as f:
    heights = np.array([
        [int(h) for h in line.strip()] for line in f.readlines()
        ])
    
# Grid dimensions
I, J = heights.shape

scenic_scores = np.zeros_like(heights)

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        
        # The outtermost trees have zero scenic score
        if (i==0) or (i==I-1) or (j==0) or (j==J-1):
            scenic_scores[i,j] = 0
        
        else:
            # Travel outwards in each direction, counting the distance to a 
            # tree of equal or greater height
            score_list = []
            for direction in [row[:j][::-1], row[j+1:], heights[:i,j][::-1], heights[i+1:,j]]:
                for k, h in enumerate(direction):
                    if h >= height:
                        break
                score_list.append(k+1)
            scenic_scores[i,j] = np.product(score_list)

print(np.max(scenic_scores))