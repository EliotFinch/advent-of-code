with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Create a list of sensor and beacon coordinate pairs
sb_pairs = []
for line in lines:
    line_coords = []
    for string in line.split(':'):
        x_str, y_str = string.split(',')
        x = int(x_str[1+x_str.index('='):])
        y = int(y_str[1+y_str.index('='):])
        line_coords.append([x,y])
    sb_pairs.append(line_coords)
    
# Create a list of sensor and beacon coordinates
sb_coords = []
for sensor, beacon in sb_pairs:
    if sensor not in sb_coords:
        sb_coords.append(sensor)
    if beacon not in sb_coords:
        sb_coords.append(beacon)
        
# Function to check if an x coordinate lies in a list of (start,end) pairs
def in_pairs(x, pairs):
    for start, end in pairs:
        if (x >= start) & (x <= end):
            return True
    return False

# The row we're focussing on
y = 2000000

# For each sensor we can rule out a segment of the chosen row. Store the 
# segments as (start,end) pairs.
pairs = []

for sensor, beacon in sb_pairs:
    
    sx, sy = sensor
    bx, by = beacon
    
    distance = abs(sx-bx) + abs(sy-by)
    
    # All positions on the grid with a distance less than this cannot have a 
    # beacon
    
    # Distance to the chosen y row
    dy = abs(sy-y)
    
    if dy <= distance:
        
        # The number of steps we can take along the chosen row (centered on the
        # sensor x coordinate) whilst keeping the distance less than or equal
        # to the distance to the beacon
        excess = distance - dy
        
        # Record x coordinates we can rule out
        pairs.append([sx-excess, sx+excess])
        
# Sort the pairs by the start values
pairs.sort(key=lambda x: x[0])

# Shift the pairs so that they start at zero. This won't change the 
# "coverage" (the quantity we're interested in).
x0 = pairs[0][0]
pairs_shift = [[n[0]-x0, n[1]-x0] for n in pairs]

# Calculate the coverage
count = 0
current_start = 0
current_end = 0
    
for i, (start, end) in enumerate(pairs_shift):
    
    if (i != 0) and (start <= current_end):
        new_end = max([current_end, end])
        count += new_end - current_end
        current_end = new_end
        
    else:
        count += end - start + 1
        current_start = start
        current_end = end

# Remove counts which overlap with a sensor or beacon
for sbx, sby in sb_coords:
    if (sby == y) and in_pairs(sbx, pairs):
        count -= 1
        
print(count)