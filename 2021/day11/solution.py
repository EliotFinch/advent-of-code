with open('input.txt') as f:
    input_grid = [list(map(int,line.strip())) for line in f.readlines()]
    
class grid_class:
    
    def __init__(self, input_grid):
        self.grid = input_grid
        
    def add_one(self):
        # Add one to all grid elements
        self.grid = [list(map(lambda n: n+1, row)) for row in self.grid]
        
    def add_to_adjacent(self, loc):
        # Add one to all points neighboring points, unless they have value 10
        i, j = loc
        for ip in [i-1,i,i+1]:
            for jp in [j-1,j,j+1]:
                if (ip not in [-1,10]) and (jp not in [-1,10]):
                    if self.grid[ip][jp] != 10:
                        self.grid[ip][jp] += 1
        
    def is_ten(self):
        # Check for the value 10 in the grid
        for row in self.grid:
            if 10 in row:
                return True
        return False
    
    def step(self):
        # Perform a step and count the flashes
        
        flashes = 0
        self.add_one()
        
        while self.is_ten():
            for i, row in enumerate(self.grid):
                for j, energy in enumerate(row):
                    if energy == 10:
                        flashes += 1
                        self.add_to_adjacent((i,j))
                        # Move this value off of 10
                        self.grid[i][j] += 1
        
        # Reset all positions that have flashed to zero
        for i, row in enumerate(self.grid):
            for j, energy in enumerate(row):
                if energy > 9:
                    self.grid[i][j] = 0
                    
        return flashes

# Part 1
# ======

grid = grid_class(input_grid)

steps = 100
flashes = 0

for step in range(steps):
    flashes += grid.step()
    
print(flashes)

# Part 2
# ======

grid = grid_class(input_grid)

step_counter = 0
while sum([sum(row) for row in grid.grid]) != 0:
    step_counter += 1
    _ = grid.step()
    
print(step_counter)