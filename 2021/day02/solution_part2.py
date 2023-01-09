horizontal_position = 0
depth = 0
aim = 0

with open('input.txt') as f:
    for entry in f:
        action, X = entry.split()
        if action == 'forward':
            horizontal_position += int(X)
            depth += int(X)*aim
        if action == 'up':
            aim -= int(X)
        if action == 'down':
            aim += int(X)

print(horizontal_position*depth)