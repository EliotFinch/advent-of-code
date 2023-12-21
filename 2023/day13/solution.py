import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Load patterns into a list of lists
string_patterns = []

previous_start = 0
for i, line in enumerate(lines):
    if line == '':
        string_patterns.append(lines[previous_start:i])
        previous_start = i + 1
string_patterns.append(lines[previous_start:])

# Convert patterns into numpy arrays
patterns = []
for pattern in string_patterns:
    patterns.append(
        np.vstack([list(line) for line in pattern])
    )

# Part 1
# ------

summary = 0

for pattern in patterns:

    # Dimensions (rows, columns) of this pattern
    R, C = pattern.shape

    # Investigate reflections between columns first
    for i in range(1, int(C/2) + 1):
        if np.all(pattern[:,:2*i] == np.fliplr(pattern[:,:2*i])):
            summary += i
            break

        if np.all(pattern[:,-2*i:] == np.fliplr(pattern[:,-2*i:])):
            summary += C-i
            break

    # Investigate reflections between rows
    for i in range(1, int(R/2) + 1):
        if np.all(pattern[:2*i,:] == np.flipud(pattern[:2*i,:])):
            summary += 100*i
            break

        if np.all(pattern[-2*i:,:] == np.flipud(pattern[-2*i:,:])):
            summary += 100*(R-i)
            break

print(summary)

# Part 2
# ------

summary = 0

for pattern in patterns:

    # Dimensions (rows, columns) of this pattern
    R, C = pattern.shape

    # Investigate reflections between columns first
    for i in range(1, int(C/2) + 1):
        if np.sum(pattern[:,:2*i] != np.fliplr(pattern[:,:2*i])) == 2:
            summary += i
            break

        if np.sum(pattern[:,-2*i:] != np.fliplr(pattern[:,-2*i:])) == 2:
            summary += C-i
            break

    # Investigate reflections between rows
    for i in range(1, int(R/2) + 1):
        if np.sum(pattern[:2*i,:] != np.flipud(pattern[:2*i,:])) == 2:
            summary += 100*i
            break

        if np.sum(pattern[-2*i:,:] != np.flipud(pattern[-2*i:,:])) == 2:
            summary += 100*(R-i)
            break

print(summary)