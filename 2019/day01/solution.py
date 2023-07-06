with open('input.txt', 'r') as f:
    data = [int(d.strip()) for d in f.readlines()]

s = 0
for d in data:
    d = int(d/3) - 2
    s += d
    
def calculate_fuel(f):
    result = int(f/3) - 2
    if result < 0:
        result = 0
    return result