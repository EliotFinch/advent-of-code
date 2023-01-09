move_key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
    }

move_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
    }

result_dict = {
    ('rock', 'scissors'): 'lose',
    ('paper', 'rock'): 'lose',
    ('scissors', 'paper'): 'lose',
    
    ('rock', 'rock'): 'draw',
    ('paper', 'paper'): 'draw',
    ('scissors', 'scissors'): 'draw',
    
    ('rock', 'paper'): 'win',
    ('paper', 'scissors'): 'win',
    ('scissors', 'rock'): 'win'
    }

result_scores = {
    'lose': 0,
    'draw': 3,
    'win': 6
    }

with open('input.txt', 'r') as f:
    strat_guide = [line.strip().split() for line in f.readlines()]

score = 0
for opponent, player in strat_guide:
    
    opponent_move = move_key[opponent]
    player_move = move_key[player]
    
    move_score = move_scores[player_move]
    result_score = result_scores[result_dict[(opponent_move, player_move)]]
    
    score += move_score + result_score
    
print(score)