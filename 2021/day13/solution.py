with open('input.txt') as f:
    
    lines = f.readlines()
    dots = []
    folds = []
    
    for line in lines:
        line = line.strip()
        if 'fold along' in line:
            folds.append(line.split()[-1])
        elif line != '':
            dots.append(tuple(int(d) for d in line.split(',')))

folded_dots = dots

for fold in folds:
    
    fold_location = int(fold.split('=')[-1])
    new_folded_dots = []
    
    for dot in folded_dots:
        if 'x' in fold:
            if dot[0] > fold_location:
                folded_dot = (2*fold_location - dot[0], dot[1])
            else:
                folded_dot = dot
        else:
            if dot[1] > fold_location:
                folded_dot = (dot[0], 2*fold_location - dot[1])
            else:
                folded_dot = dot
        new_folded_dots.append(folded_dot)
        
    folded_dots = new_folded_dots
    # print(len(set(folded_dots)))
    
folded_dots = set(folded_dots)

max_x = 0
max_y = 0

for x, y in folded_dots:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
        
output = [(max_x+1)*[0] for _ in range(max_y+1)]

for x, y in folded_dots:
    output[y][x] = 1
    
output_lines = []
for line in output:
    line_str = ''.join(str(d) for d in line)
    output_lines.append(line_str.replace('0','.').replace('1','#'))
    
with open('output.txt', 'w') as f:
    f.write('\n'.join(output_lines))