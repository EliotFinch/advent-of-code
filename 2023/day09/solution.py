import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

histories = []
for line in lines:
    history = np.array([int(x) for x in line.split()])
    histories.append(history)
histories = np.array(histories)

# Part 1
# ------

extrapolated_values = []

for history in histories:
    
    last_values = [history[-1]]

    diffs = np.diff(history)
    last_values.append(diffs[-1])

    while not all(diffs == 0):
        diffs = np.diff(diffs)
        last_values.append(diffs[-1])

    extrapolated_values.append(sum(last_values))

print(sum(extrapolated_values))

# Part 2
# ------

extrapolated_values = []

for history in histories:
    
    first_values = [history[0]]

    diffs = np.diff(history)
    first_values.append(diffs[0])

    while not all(diffs == 0):
        diffs = np.diff(diffs)
        first_values.append(diffs[0])

    # We now need to alternate the signs in the sum
    sign_array = np.ones(len(first_values), dtype=int)
    sign_array[1::2] = -1

    extrapolated_values.append(np.sum(first_values*sign_array))

print(sum(extrapolated_values))