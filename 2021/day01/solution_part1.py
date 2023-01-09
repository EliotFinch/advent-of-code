count = 0

with open('input.txt') as f:
    previous = 0
    for entry in f:
        if int(entry) > previous:
            count += 1
        previous = int(entry)

print(count-1)