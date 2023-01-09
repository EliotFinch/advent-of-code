from itertools import permutations


# Load input
# ----------

# Load input into a dict of the form {room: [flow rate, connected rooms]}
rooms = {}

with open('input.txt') as f:
    for line in f.readlines():
        
        room_rate, connections_str = [l.strip() for l in line.split(';')]
        
        room = room_rate[6:8]
        rate = int(room_rate[1+room_rate.index('='):])
        
        connections = [c[-2:] for c in connections_str.split(',')]
        
        rooms[room] = [rate, connections]


# Simplify the problem to a smaller set of nodes and weights
# ----------------------------------------------------------

# We only care about the start room and rooms with a non-zero flow rate
nodes = set([room for room in rooms.keys() if rooms[room][0] > 0] + ['AA'])

# Pre-compute the distance between all these chosen rooms (and the start room)
weights = {}

# Perform a walk (as in day 12) to find the shortest path between the rooms
for pair in permutations(nodes, r=2):
    
    start, end = pair
    
    paths = [[start]]
    visited = [start]

    while end not in visited:
        
        # A list of new paths with all possible steps from the current paths
        new_paths = []
        
        for path in paths:
            
            current_node = path[-1]
            proposed_steps = rooms[current_node][1]
            
            for proposed_step in proposed_steps:
                
                # We don't want to visit previously visited rooms
                if proposed_step not in visited:
                    new_paths.append(path + [proposed_step])
                    visited.append(proposed_step)
                
        paths = new_paths
    
    # Get the distance of the path which reached the end first
    for path in paths:
        if end in path:
            weights[pair] = len(path) - 1


# Function to explore all possible paths in a given time
# ------------------------------------------------------

def walk(nodes, weights, start, time):
    
    # Explore every possible order of turning on the valves, stopping when we 
    # reach the time limit
    
    # A dictionary of paths with (time remaining, current flow rate, pressure 
    # released)
    paths = {(start,): (time, 0, 0)}
    
    # A dictionary of finished paths with (final flow rate, final pressure 
    # released)
    finished_paths = {}
    
    while len(paths) > 0:
        
        new_paths = {}
        
        for path, info in paths.items():
            
            visited = set(path)
            current_room = path[-1]
            unvisited = nodes.difference(visited)
            
            if len(unvisited) > 0:
            
                for next_room in unvisited:
                    
                    time_remaining, flow_rate, pressure_released = info
                    w = weights[(current_room, next_room)]
                    
                    if w < time_remaining:
                        
                        # Tavel to next room
                        time_remaining -= w
                        pressure_released += w*flow_rate
                        
                        # Turn on new valve
                        time_remaining -= 1
                        pressure_released += flow_rate
                        flow_rate += rooms[next_room][0]
                        
                        # Store current state
                        new_paths[path + (next_room,)] = (
                            time_remaining, flow_rate, pressure_released
                            )
                        
                    else:
                        
                        # There is not enough time to visit the next roon, so 
                        # calculate the pressure released in the remaining 
                        # time and finish the path
                        pressure_released += time_remaining*flow_rate
                        finished_paths[path] = (flow_rate, pressure_released)
                        
            else:
                
                # All rooms have been visited. Calculate the pressure released 
                # in the remaining time.
                
                time_remaining, flow_rate, pressure_released = info
                pressure_released += time_remaining*flow_rate
                finished_paths[path] = (flow_rate, pressure_released)
                    
        paths = new_paths
        
    return finished_paths


# Part 1
# ------

finished_paths = walk(nodes, weights, 'AA', 30)
print(max([v[1] for v in finished_paths.values()]))


# Part 2
# ------

# For our input we can never reach all rooms in the time allowed, so the
# optimal solution will consist of two paths which don't overlap

finished_paths = walk(nodes, weights, 'AA', 26)

# To speed things up we can just consider the "best" paths which release the
# most pressure
best_paths = {}
for visited, info in finished_paths.items():
    flow_rate, pressure_released = info
    if pressure_released > 1000:
        best_paths[visited] = (flow_rate, pressure_released)
finished_paths = best_paths

max_pressure = 0

# For each path find all other paths that don't overlap and add up the 
# pressure released
for visited, info in finished_paths.items():
    
    visited = set(visited)
    flow_rate, pressure_released = info
    
    for second_visited, second_info in finished_paths.items():
        
        second_visisted = set(second_visited)
        second_flow_rate, second_pressure_released = second_info
        
        if len(visited.intersection(second_visited)) == 1:
            summed_pressure_release = pressure_released + second_pressure_released
            if summed_pressure_release > max_pressure:
                max_pressure = summed_pressure_release

print(max_pressure)
