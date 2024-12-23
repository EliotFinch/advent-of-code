import re

with open('input.txt', 'r') as f:
    memory = ''.join(f.readlines())

# Part One
# --------

result = 0
for operation in re.finditer(r'mul\((\d+),(\d+)\)', memory):
    result += int(operation.group(1))*int(operation.group(2))

print(result)

# Part Two
# --------

# Test if a string begins (^) with the mul pattern
mul_pattern = re.compile(r'^mul\((\d+),(\d+)\).*')

# Fkag for whether multiplying is turned on
multiply_flag = True

result = 0
for i in range(len(memory)):
    current_string = memory[i:]
    if multiply_flag and current_string.startswith('mul('):
        match = mul_pattern.search(current_string)
        if match:
            result += int(match.group(1))*int(match.group(2))
    elif current_string.startswith('do()'):
        multiply_flag = True
    elif current_string.startswith("don't()"):
        multiply_flag = False

print(result)
