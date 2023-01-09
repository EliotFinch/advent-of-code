with open('input.txt') as f:
    connections = [line.strip().split('-') for line in f.readlines()]
    
caves = set([cave for pair in connections for cave in pair])
small_caves = [cave for cave in caves if cave.lower() == cave]
        
paths = [['start']]

finished = False

while not finished:
    
    new_paths = []

    for path in paths:
        if 'end' not in path:
            current_position = path[-1]
            for pair in connections:
                if current_position in pair:
                    next_cave = pair[1-pair.index(current_position)]
                    if next_cave in small_caves:
                        if next_cave != 'start':
                            visits = path.count(next_cave)
                            if visits == 0:
                                new_paths.append(path + [next_cave])
                            elif not [path.count(cave) for cave in small_caves].count(2):
                                new_paths.append(path + [next_cave])
                    else:
                        new_paths.append(path + [next_cave])
        else:
            new_paths.append(path)
        
    if new_paths == paths:
        finished = True
    else:
        paths = new_paths
        
print(len(paths))