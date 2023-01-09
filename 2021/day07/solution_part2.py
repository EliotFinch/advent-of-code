with open('input.txt') as f:
    positions = [int(pos) for pos in f.readlines()[0].split(',')]

min_fuel = 1e10
min_target = 0

for target_pos in range(min(positions), max(positions)):

    fuel_use = 0
    for pos in positions:
        distance = abs(target_pos-pos)
        fuel_use += distance*(distance+1)/2
        
    if fuel_use < min_fuel:
        min_fuel = fuel_use
        min_target = target_pos
        
print(min_fuel)