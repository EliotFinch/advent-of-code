horizontal_position = 0
depth = 0

with open('input.txt') as f:
    for entry in f:
        action, X = entry.split()
        if action == 'forward':
            horizontal_position += int(X)
        if action == 'up':
            depth -= int(X)
        if action == 'down':
            depth += int(X)

print(horizontal_position*depth)