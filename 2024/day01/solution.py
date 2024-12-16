import numpy as np

# Part One
# --------

left_list = []
right_list = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        location_IDs = [int(ID) for ID in line.split()]
        left_list.append(location_IDs[0])
        right_list.append(location_IDs[1])

left_list = np.array(left_list)
right_list = np.array(right_list)

print(np.sum(np.abs(np.sort(left_list)-np.sort(right_list))))

# Part Two
# --------

similarity_score = 0

for left_location_ID in left_list:
    multiplier = 0
    for right_location_ID in right_list:
        if left_location_ID == right_location_ID:
            multiplier += 1
    similarity_score += multiplier*left_location_ID

print(similarity_score)
