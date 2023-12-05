class engine:

    def __init__(self, schematic):
        self.schematic = schematic

        # Store numbers of rows and columns in the schematic
        self.nrows = len(self.schematic)
        self.ncols = len(self.schematic[0])

        # Find the coordinates of each number in the schematic
        self.get_numbers()

    def get_numbers(self):
        
        # A list of tuples of the form (row, column, number length, number)
        # where row and column are the index of the first digit in the number
        self.numbers = []
        for j, row in enumerate(self.schematic):
            for i, character in enumerate(row):
                if character.isdigit():
                    # Check that this isn't part of a number we've already found
                    if (j,i) not in [(n[0], ip) for n in self.numbers for ip in range(n[1], n[1]+n[2])]:
                    # Find the length of the number
                        length = 1
                        while (i+length < self.ncols) and (row[i+length].isdigit()):
                            length += 1
                        self.numbers.append((j, i, length, int(row[i:i+length])))
    
    def get_adjacent(self, row, col):
        # Get all adjacent characters to the index (row, column)
        adjacent = {}
        for rowi in [row-1, row, row+1]:
            for coli in [col-1, col, col+1]:
                if rowi in [-1, self.nrows]:
                    continue
                if coli in [-1, self.ncols]:
                    continue
                if (rowi==row) & (coli==col):
                    continue
                adjacent[(rowi,coli)] = self.schematic[rowi][coli]
        return adjacent
    
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

e = engine(lines)

# Part 1
# ------

# A number is a part number if it is adjacent to a symbol
part_numbers = []
for j, i, length, number in e.numbers:
    part_number = False
    for ip in range(i, i+length):
        adjacent_characters = e.get_adjacent(j, ip)
        if (
            (part_number == False) & 
            (not all((character == '.') or (character.isdigit()) for character in adjacent_characters.values()))
           ):
            part_number = True
            part_numbers.append(int(number))

print(sum(part_numbers))

# Part 2
# ------

from collections import defaultdict

star_dict = defaultdict(list)
for j, i, length, number in e.numbers:
    # Lets assume each number is only associated with at most one star
    number_added = False
    for ip in range(i, i+length):
        adjacent_characters = e.get_adjacent(j, ip)
        for coord, character in adjacent_characters.items():
            if (character == '*') & (number_added == False):
                star_dict[coord].append(int(number))
                number_added = True

gear_ratios = []
for number_list in star_dict.values():
    # Gears have multiple numbers associated with them:
    if len(number_list) > 1:
        gear_ratios.append(number_list[0]*number_list[1])

print(sum(gear_ratios))