opponent_moves = ['A', 'B', 'C']
player_moves = ['X', 'Y', 'Z']

with open('input.txt', 'r') as f:
    strat_guide = [line.strip().split() for line in f.readlines()]

score = 0
for opponent, player in strat_guide:
    
    i = opponent_moves.index(opponent)
    j = player_moves.index(player)
    
    move_score = j + 1
    result_score = [3,0,6][(i-j)%3]
    
    score += move_score + result_score
    
print(score)