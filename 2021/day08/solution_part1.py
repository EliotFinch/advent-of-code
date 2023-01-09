with open('input.txt') as f:
    lines = f.readlines()
    
    patterns = []
    outputs = []
    
    for line in lines:
        pattern, output = line.strip().split('|')
        patterns.append(pattern.split())
        outputs.append(output.split())
        
easy_digit_count = 0
for output in outputs:
    for digit in output:
        if (len(digit) == 2) | (len(digit) == 4) | (len(digit) == 3) | (len(digit) == 7):
            easy_digit_count += 1

print(easy_digit_count)