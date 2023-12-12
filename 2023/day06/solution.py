with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Part 1
# ------

# Get a list of available times, and a list of records
times_available, records = lines
times_available = [int(time) for time in times_available.split()[1:]]
records = [int(distance) for distance in records.split()[1:]]

# We can simply calculate the distance travelled for each hold time, and filter
# out which ones give a distance greater than the record

# Number of ways to beat the record (a list of hold times)
n_ways = []

for time_available, record in zip(times_available, records):
    distances = []
    for hold_time in range(1, time_available):
        travel_time = time_available - hold_time
        distance_travelled = travel_time*hold_time
        distances.append(distance_travelled)
    n_ways.append(len([distance for distance in distances if distance > record]))

product = 1
for i in n_ways:
    product *= i
    
print(product)

# Part 2
# ------

# Re-read the input as a single time available and a single record
time_available, record = lines
time_available = int(''.join(time for time in time_available.split()[1:]))
record = int(''.join(distance for distance in record.split()[1:]))

# We have to avoid loops with such large ranges. We can rewrite the problem as
# follows:

# distance_travelled = speed*time 
#                    = hold_time*(time_available - hold_time)
#                    = -hold_time**2 + time_available*hold_time

# We require that distance_travlled > record. This gives us a quadratic 
# equation, for which the roots are the lower and upper hold times that beat
# the record.

# The max and min hold times given by
# hold_time**2 - time_available*hold_time + record = 0

# Applying the quadratic formula...
# hold_time_maxmin = (time_available +- (time_available**2 - 4*record)**(1/2))/2

min_hold_time = (time_available - (time_available**2 - 4*record)**(1/2))/2
max_hold_time = (time_available + (time_available**2 - 4*record)**(1/2))/2

# We need to round the min_hold_time up:
min_hold_time = int(min_hold_time) + 1

# And the max_hold_time down:
max_hold_time = int(max_hold_time)

# Then we can get the number of ways of beating the record
print(max_hold_time - min_hold_time + 1)