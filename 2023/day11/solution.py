import itertools

with open('input.txt', 'r') as f:
    image = f.read().splitlines()

nrows = len(image)
ncols = len(image[0])

# Find the (row, column) coordinates of all galaxies
galaxies = []
for i, row in enumerate(image):
    for j, pixel in enumerate(row):
        if pixel == '#':
            galaxies.append((i, j))

# Find the indices of all empty rows and colmns
            
empty_rows = []
for i, row in enumerate(image):
    if all(pixel == '.' for pixel in row):
        empty_rows.append(i)

empty_columns = []
for j in range(len(image[0])):
    if all(row[j] == '.' for row in image):
        empty_columns.append(j)

def sum_lengths(expansion):
    """
    Return the sum of the lengths of all the paths between galaxies, where
    the length of a path is the sum of the Manhattan distances between
    galaxies. The distance in each direction is increased by the specified 
    expansion factor if there is an empty row or column between them.
    """

    length_sum = 0

    # Consider every possible pair of galaxies
    for coord1, coord2 in itertools.combinations(galaxies, 2):

        row1, column1 = coord1
        row2, column2 = coord2

        # Sort the rows
        if row1 > row2:
            row1, row2 = row2, row1

        # Sort the columns
        if column1 > column2:
            column1, column2 = column2, column1

        # If the galaxies are either side of an empty row or column, then we
        # need to expand the distance between them by the requested factor
            
        row_expansion = 0
        for empty_row_index in empty_rows:
            if row1 < empty_row_index < row2:
                row_expansion += expansion - 1

        column_expansion = 0
        for empty_column_index in empty_columns:
            if column1 < empty_column_index < column2:
                column_expansion += expansion - 1

        drow = abs(coord2[0] - coord1[0]) + row_expansion
        dcol = abs(coord2[1] - coord1[1]) + column_expansion

        length_sum += drow + dcol

    return length_sum

# Part 1
# ------

print(sum_lengths(2))

# Part 2
# ------

print(sum_lengths(1000000))