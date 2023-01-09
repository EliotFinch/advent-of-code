with open('input.txt') as f:
    lines = f.readlines()
    
    patterns = []
    outputs = []
    
    for line in lines:
        pattern, output = line.strip().split('|')
        patterns.append(pattern.split())
        outputs.append(output.split())

digit_maps = []
for pattern, output in zip(patterns, outputs):
    
    temp_map = {}
    
    for digit in pattern+output:
        
        digit = ''.join(sorted(digit))
        
        if len(digit) == 2:
            temp_map[1] = digit
        elif len(digit) == 4:
            temp_map[4] = digit
        elif len(digit) == 3:
            temp_map[7] = digit
        elif len(digit) == 7:
            temp_map[8] = digit
        
    for digit in pattern+output:
        
        digit = ''.join(sorted(digit))
        
        if (len(digit) == 5) & (all([c in digit for c in temp_map[1]])):
            temp_map[3] = digit
        elif (len(digit) == 6) & (all([c in digit for c in temp_map[4]])):
            temp_map[9] = digit
        elif (len(digit) == 6) & (all([c in digit for c in temp_map[1]])):
            temp_map[0] = digit
        elif len(digit) == 6:
            temp_map[6] = digit
            
    for digit in pattern+output:
        
        digit = ''.join(sorted(digit))
            
        if (len(digit) == 5) & (all([c in temp_map[6] for c in digit])):
            temp_map[5] = digit
        if (len(digit) == 5) & (not all([c in temp_map[6] for c in digit])) & \
            (not all([c in digit for c in temp_map[1]])):
            temp_map[2] = digit
            
    digit_maps.append(temp_map)
    
reversed_digit_maps = []
for digit_map in digit_maps:
    reversed_digit_maps.append(dict((v,k) for k,v in digit_map.items()))

converted_outputs = []
for digit_map, output in zip(reversed_digit_maps, outputs):
    converted_digit = ''
    for digit in output:
        digit = ''.join(sorted(digit))
        converted_digit += str(digit_map[digit])
    converted_outputs.append(int(converted_digit))
    
print(sum(converted_outputs))