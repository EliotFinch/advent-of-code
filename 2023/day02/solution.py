with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Load the data into a dictionary. Each key is the game number, and each value
# is a list of games of the form 
# # [{'red': nred0, 'green': ngreen0, 'blue': nblue0}, {'red': nred1, 'green': ngreen1, 'blue': nblue1}, ...]
game_dict = {}

for line in lines:
    game_number, games = line.split(':')
    game_number = int(game_number[5:])
    games = [game.strip() for game in games.split(';')]

    game_dict[game_number] = []

    for game in games:
        result_dict = {}
        for colour_count in game.split(','):
            count, colour = colour_count.split()
            if 'red' in colour:
                result_dict['red'] = int(count)
            elif 'green' in colour:
                result_dict['green'] = int(count)
            else:
                result_dict['blue'] = int(count)
        game_dict[game_number].append(result_dict)

# Part 1
# ------

max_counts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

allowed_IDs = []

for ID, result in game_dict.items():
    allowed = True
    for game in result:
        for colour, count in game.items():
            if count > max_counts[colour]:
                allowed = False

    if allowed:
        allowed_IDs.append(ID)


print(sum(allowed_IDs))

# Part 2
# ------

power_list = []

for ID, result in game_dict.items():

    max_colour_count = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for game in result:
        for colour, count in game.items():
            if count > max_colour_count[colour]:
                max_colour_count[colour] = count
    
    p = 1
    for count in max_colour_count.values():
        p *= count
    power_list.append(p)

print(sum(power_list))