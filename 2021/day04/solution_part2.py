with open('input.txt') as f:
    
    lines = f.readlines()
    
    board_dict = {}
    board_counter = -1
    
    for i, line in enumerate(lines):
        
        line = line.rstrip()
        
        if i == 0:
            draws = [int(draw) for draw in line.split(',')]
        elif line == '':
            board_counter += 1
            board_dict[board_counter] = []
        else:
            board_dict[board_counter].append([int(n) for n in line.split()])
            
class board():
    
    def __init__(self, grid):
        self.grid = grid
        self.marked_grid = [5*[0] for _ in range(5)]
            
    def marked_row(self, n):
        return self.marked_grid[n]
    
    def marked_column(self, n):
        out = []
        for row in self.marked_grid:
            out.append(row[n])
        return out
            
    def mark(self, number):
        for i, row in enumerate(self.grid):
            if number in row:
                self.marked_grid[i][row.index(number)] = 1
                
    def check(self):
        for i in range(5):
            if (sum(self.marked_row(i)) == 5) | (sum(self.marked_column(i)) == 5):
                return True
        return False

boards = []
for grid in board_dict.values():
    boards.append(board(grid)) 
completed = len(boards)*[0]
       
for draw in draws:
    for i, board in enumerate(boards):
        if not completed[i]:
            board.mark(draw)
            if board.check():
                completed[i] = 1
                winner = i
                winning_draw = draw
        
winning_board = boards[winner]
unmarked_numbers = []

for i, row in enumerate(winning_board.marked_grid):
    for j, number in enumerate(row):
        if number == 0:
            unmarked_numbers.append(winning_board.grid[i][j])
            
print(sum(unmarked_numbers)*winning_draw)