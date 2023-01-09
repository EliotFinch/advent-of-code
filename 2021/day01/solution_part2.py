count = 0

with open('input.txt') as f:
    data = [int(entry.rstrip()) for entry in f.readlines()]

window_length = 3
windowed_data = []

for i in range(len(data)-window_length+1):
    window_sum = sum(data[i:i+window_length])
    windowed_data.append(window_sum)
    
count = 0
previous = 0

for entry in windowed_data:
    if int(entry) > previous:
        count += 1
    previous = int(entry)

print(count-1)