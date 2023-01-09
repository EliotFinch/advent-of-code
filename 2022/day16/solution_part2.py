from itertools import permutations

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

max_pressure = 0

# The number of rooms I visit
for r in range(1, len(rooms)):
    
    for rooms_I_visit in permutations(rooms, r=r):

        # Explore every possible order of turning on the valves, stopping when we 
        # reach the time limit
        
        rooms_I_visit = set(list(rooms_I_visit) + ['AA'])
        
        # A dictionary of paths (expressed as a concatenation of rooms names) with
        # (time remaining, current flow rate, pressure released)
        paths = {'AA': (26, 0, 0)}
        
        finished_paths = {}
        
        while len(paths) > 0:
            
            new_paths = {}
            
            for path, info in paths.items():
                
                visited = set([path[i:i+2] for i in range(0, len(path)-1, 2)])
                current_room = path[-2:]
                
                unvisited = rooms_I_visit.difference(visited)
                
                if len(unvisited) > 0:
                
                    for next_room in unvisited:
                        
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
        
        my_max_pressure = max([v[1] for v in finished_paths.values()])
        
        rooms_elephant_visits = set(list(set(rooms).difference(rooms_I_visit)) + ['AA'])
        
        # A dictionary of paths (expressed as a concatenation of rooms names) with
        # (time remaining, current flow rate, pressure released)
        paths = {'AA': (26, 0, 0)}
        
        finished_paths = {}
        
        while len(paths) > 0:
            
            new_paths = {}
            
            for path, info in paths.items():
                
                visited = set([path[i:i+2] for i in range(0, len(path)-1, 2)])
                current_room = path[-2:]
                
                unvisited = rooms_elephant_visits.difference(visited)
                
                if len(unvisited) > 0:
                
                    for next_room in unvisited:
                        
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
        
        elephant_max_pressure = max([v[1] for v in finished_paths.values()])
        
        if my_max_pressure + elephant_max_pressure > max_pressure:
            max_pressure = my_max_pressure + elephant_max_pressure
