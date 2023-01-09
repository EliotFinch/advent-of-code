move_key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    }

move_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
    }

move_dict = {
    ('rock', 'lose'): 'scissors',
    ('paper', 'lose'): 'rock',
    ('scissors', 'lose'): 'paper',
    
    ('rock', 'draw'): 'rock',
    ('paper', 'draw'): 'paper',
    ('scissors', 'draw'): 'scissors',
    
    ('rock', 'win'): 'paper',
    ('paper', 'win'): 'scissors',
    ('scissors', 'win'): 'rock'
    }

result_key = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
    }

result_scores = {
    'lose': 0,
    'draw': 3,
    'win': 6
    }

with open('input.txt', 'r') as f:
    strat_guide = [line.strip().split() for line in f.readlines()]

score = 0
for opponent, outcome in strat_guide:
    
    opponent_move = move_key[opponent]
    outcome = result_key[outcome]
    
    result_score = result_scores[outcome]
    
    player_move = move_dict[(opponent_move, outcome)]
    move_score = move_scores[player_move]
    
    score += move_score + result_score
    
print(score)