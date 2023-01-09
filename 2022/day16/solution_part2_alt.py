from itertools import permutations
from tqdm import tqdm

# Load input into a dict of the form {room: [flow rate, connected rooms]}
valves = {}

with open('input.txt') as f:
    for line in f.readlines():
        
        room_rate, connections_str = [l.strip() for l in line.split(';')]
        
        room = room_rate[6:8]
        rate = int(room_rate[1+room_rate.index('='):])
        
        connections = [c[-2:] for c in connections_str.split(',')]
        
        valves[room] = [rate, connections]

# We only care about rooms with a non-zero flow rate
rooms = [room for room in valves.keys() if valves[room][0] > 0]

# Pre-compute the distance between all these rooms (and the start room)
distances = {}

# Perform a walk (as in day 12) to find the shortest path between the rooms
for pair in permutations(rooms + ['AA'], r=2):
    
    start, end = pair
    
    paths = [[start]]
    visited = [start]

    while end not in visited:
        
        # A list of new paths with all possible steps from the current paths
        new_paths = []
        
        for path in paths:
            
            current_room = path[-1]
            proposed_steps = valves[current_room][1]
            
            for proposed_step in proposed_steps:
                
                # We don't want to visit previously visited rooms
                if proposed_step not in visited:
                    new_paths.append(path + [proposed_step])
                    visited.append(proposed_step)
                
        paths = new_paths
    
    # Get the distance of the path which reached the end first
    for path in paths:
        if end in path:
            distances[pair] = len(path) - 1

# Explore every possible order of turning on the valves, stopping when we 
# reach the time limit

rooms = set(rooms + ['AA'])

# A dictionary of paths (expressed as a concatenation of rooms names) with
# (time remaining, current flow rate, pressure released)
paths = {'AA': (26, 0, 0)}

finished_paths = {}

while len(paths) > 0:
    
    new_paths = {}
    
    for path, info in paths.items():
        
        visited = set([path[i:i+2] for i in range(0, len(path)-1, 2)])
        current_room = path[-2:]
        
        unvisited = rooms.difference(visited)
        
        if len(unvisited) > 0:
        
            for next_room in rooms.difference(visited):
                
                time_remaining, flow_rate, pressure_released = info
                
                d = distances[(current_room, next_room)]
                
                if d < time_remaining:
                    
                    # Tavel to next room
                    time_remaining -= d
                    pressure_released += d*flow_rate
                    
                    # Turn on new valve
                    time_remaining -= 1
                    pressure_released += flow_rate
                    flow_rate += valves[next_room][0]
                    
                    # Store current state
                    new_paths[path + next_room] = (time_remaining, flow_rate, pressure_released)
                    
                else:
                    
                    pressure_released += time_remaining*flow_rate
                    
                    finished_paths[path] = (flow_rate, pressure_released)
                    
        else:
            
            # All rooms have been visited. Calculate the pressure released in
            # the remainig time
            
            time_remaining, flow_rate, pressure_released = info
            
            pressure_released += time_remaining*flow_rate
            
            finished_paths[path] = (flow_rate, pressure_released)
                
    paths = new_paths
    
max_pressure = 0

frozen_paths = {}

for path, info in finished_paths.items():
    visited = tuple([path[i:i+2] for i in range(0, len(path)-1, 2)])
    frozen_paths[visited] = info

for visited, info in tqdm(frozen_paths.items()):
    
    visited = set(visited)
    flow_rate, pressure_released = info
    
    for second_visited, second_info in frozen_paths.items():
        
        second_visisted = set(second_visited)
        second_flow_rate, second_pressure_released = second_info
        
        if len(visited.intersection(second_visited)) == 1:
            if pressure_released + second_pressure_released > max_pressure:
                max_pressure = pressure_released + second_pressure_released
                
print(max_pressure)