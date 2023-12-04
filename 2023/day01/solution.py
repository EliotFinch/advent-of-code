with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

digit_dict = {
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5,
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9
    }

def find_first_last_digit(line):
    for i, character in enumerate(line):
        if character.isdigit():
            break
    for j, character in enumerate(line[::-1]):
        if character.isdigit():
            break
    return i, len(line) - 1 - j

def find_first_last_spelled_digit(line):
    occurrences = []
    for digit in digit_dict.keys():
        i = line.find(digit)
        while i != -1:
            occurrences.append((i, digit))
            i = line.find(digit, i + 1)
    sorted_occurrences = sorted(occurrences, key=lambda x: x[0])   
    return sorted_occurrences[0], sorted_occurrences[-1]

# Part One
# --------

calibration_values = []
for line in lines:
    first_digit_index, last_digit_index = find_first_last_digit(line)
    calibration_values.append(
        int(line[first_digit_index] + line[last_digit_index])
        )

print(sum(calibration_values))

# Part Two
# --------

calibration_values = []

for line in lines:

    # Find the first and last numeric digits first
    first_digit_index, last_digit_index = find_first_last_digit(line)
    first_digit, last_digit = line[first_digit_index], line[last_digit_index]

    # Then the first and last spelled digits, if present
    if any(digit in line for digit in digit_dict.keys()):

        first_spelled_digit, last_spelled_digit = find_first_last_spelled_digit(line)

        # And compare which ones are the true first and last digits
        if first_spelled_digit[0] < first_digit_index:
            first_digit = str(digit_dict[first_spelled_digit[1]])
        if last_spelled_digit[0] > last_digit_index:
            last_digit = str(digit_dict[last_spelled_digit[1]])

    calibration_values.append(
        int(first_digit + last_digit)
        )

print(sum(calibration_values))