
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Extract seeds as a list
seeds = [int(seed) for seed in lines[0].split()[1:]]

# Get the map information into a dict. Keys are the map name (e.g. 
# 'seed-to-soil'), and values are a list of tuples of the form
# (destination range start, source range start, range length)
from collections import defaultdict

default_map_dict = defaultdict(list)

for line in lines[2:]:
    if 'map' in line:
        key = line.split()[0]
    elif line == '':
        pass
    else:
        destination_range_start, source_range_start, range_length = [
            int(n) for n in line.split()
            ]
        default_map_dict[key].append(
            (destination_range_start,
            source_range_start,
            range_length)
            )

# Reformat map_dict to have keys in the form 
# (source range start, source range end, shift)
map_dict_with_gaps = {}

for key, values in default_map_dict.items():
    map_dict_with_gaps[key] = []
    for destination_range_start, source_range_start, range_length in values:     
        source_range_end = source_range_start + range_length - 1
        shift = destination_range_start - source_range_start  
        map_dict_with_gaps[key].append((source_range_start, source_range_end, shift))

    # Also sort the (source range start, source range end, shift) tuples in
    # order of the source range start
    map_dict_with_gaps[key].sort(key = lambda x: x[0])


# Remove any gaps in the map and replace with an interval with zero shift
map_dict = {}

for key, values in map_dict_with_gaps.items():
    map_dict[key] = []
    for i, (map_start, map_end, shift) in enumerate(values):
        if i == 0:
            previous_map_end = map_end
        else:
            if map_start - previous_map_end != 1:
                map_dict[key].append((previous_map_end + 1, map_start - 1, 0))
            previous_map_end = map_end
        map_dict[key].append((map_start, map_end, shift))

# Part 1
# ------

# Map each seed to get a final location

locations = []

for seed in seeds:
    for map_name, maps in default_map_dict.items():
        mapped = False
        for destination_range_start, source_range_start, range_length in maps:
            if (
                (source_range_start <= seed < source_range_start + range_length) &
                (mapped == False)
               ):
                seed = seed + destination_range_start - source_range_start
                mapped = True
    locations.append(seed)

print(min(locations))

# Part 2
# ------

# We only map the first and last value of each seed range. This involves
# keeping track of ranges splitting into multiple new ranges. 

# First convert our list of seeds into a list of seeds ranges. We have a list
# of first values in the ranges, and a list of last values in the ranges.
# These should be the same length.
seed_start_range = []
seed_end_range = []

for i in range(len(seeds)//2):

    seed_start, seed_length = seeds[2*i:2*i+2]
    seed_end = seed_start + seed_length - 1

    seed_start_range.append(seed_start)
    seed_end_range.append(seed_end)

seed_start_range.sort()
seed_end_range.sort()

# Iterate through the maps. At each iteration we process the seed ranges and 
# create a new list of seed ranges to pass to the next map.
for map_name, maps in map_dict.items(): 

    new_seed_start_range = []
    new_seed_end_range = []

    for seed_start, seed_end in zip(seed_start_range, seed_end_range, strict=True):

        # We first check if the seed range occurs inside the map range (the 
        # seed range could extend beyond the range of values that the map 
        # transforms). If these variables remain None, then the seed range 
        # extends beyond the map range.
        start_range_index = None
        end_range_index = None

        # Identify whether and where the seed start and end occurs in the map 
        for i, (map_start, map_end, shift) in enumerate(maps):
            if (map_start <= seed_start <= map_end) & (start_range_index is None):
                start_range_index = i
                # We also apply the mapping at this point:
                seed_start += shift
            if (map_start <= seed_end <= map_end) & (end_range_index is None):
                end_range_index = i
                seed_end += shift

        if start_range_index is not None:

            # Case 1: the seed range is contained within the map range
            if end_range_index is not None:

                # The new seed ranges consist of all the ranges in the map
                # contained within the seed range (basically, be careful with 
                # list slicing). The n[0] + n[2] step is applying the shift to 
                # each new range.
                new_seed_start_range += [seed_start] + [
                    n[0] + n[2] for n in maps[start_range_index+1:end_range_index+1]
                    ]
                new_seed_end_range += [
                    n[1] + n[2] for n in maps[start_range_index:end_range_index]
                    ] + [seed_end]
                
            # Case 2: the seed range starts within the map range, but extends
            # beyond it
            elif end_range_index is None:

                new_seed_start_range += [seed_start] + [
                    n[0] + n[2] for n in maps[start_range_index+1:]
                    ] + [maps[-1][0]+1]
                new_seed_end_range += [
                    n[1] + n[2] for n in maps[start_range_index:]
                    ] + [seed_end]

        elif start_range_index is None:

            # Case 3: the seed range starts outside (before) the map range, but 
            # extends into it
            if end_range_index is not None:

                new_seed_start_range += [seed_start] + [
                    n[0] + n[2] for n in maps[:end_range_index+1]
                    ]
                new_seed_end_range += [maps[0][0]-1] + [
                    n[1] + n[2] for n in maps[:end_range_index]
                    ] + [seed_end]
                
            # Case 4: the seed range starts outside (after) the map range. We
            # do not consider the case of the seed range starting before the
            # map range and ending after the map range.
            elif end_range_index is None:
                new_seed_start_range += [seed_start]
                new_seed_end_range += [seed_end]

    seed_start_range = new_seed_start_range
    seed_end_range = new_seed_end_range

print(min(seed_start_range))