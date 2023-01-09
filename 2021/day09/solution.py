with open('input.txt') as f:
    hmap = [[int(h) for h in row.strip()] for row in f.readlines()]

size = len(hmap)
    
# Border with nines to deal with edgecases
for row in hmap:
    row.insert(0,9)
    row.append(9)
    
hmap.insert(0,(size+2)*[9])
hmap.append((size+2)*[9])

lowpoints = {}
    
for i, row in enumerate(hmap):
    for j, h in enumerate(row):
        if (i not in [0,size+1]) & (j not in [0,size+1]):
            if (h < hmap[i-1][j]) & (h < hmap[i][j+1]) & (h < hmap[i+1][j]) & (h < hmap[i][j-1]):
                lowpoints[i,j] = h
                
print(sum([h + 1 for h in lowpoints.values()]))

basin_sizes = []

for i0, j0 in lowpoints.keys():
    explored = [(i0,j0)]
    new_points = True
    while new_points:
        for i, j in explored:
            for proposal in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if (hmap[proposal[0]][proposal[1]] != 9) & (proposal not in explored):
                    explored.append(proposal)
                else:
                    new_points = False
    basin_sizes.append(len(explored))

product = 1
largest_sizes = sorted(basin_sizes)[-3:]

for s in largest_sizes:
    product *= s
    
print(product)