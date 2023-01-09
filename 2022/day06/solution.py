with open('input.txt') as f:
    datastream = f.readline().strip()

distinct_chars = 14
for i in range(0, len(datastream)-(distinct_chars-1)):
    if len(set(datastream[i:i+distinct_chars])) == distinct_chars:
        print(i+distinct_chars)
        break