with open('input.txt') as f:
    positions = [int(pos) for pos in f.readlines()[0].split(',')]

target_pos = sorted(positions)[int(len(positions)/2)]

fuel_use = 0
for pos in positions:
    fuel_use += abs(target_pos-pos)