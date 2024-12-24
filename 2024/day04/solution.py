import numpy as np

with open('input.txt', 'r') as f:
    puzzle_data = [line.strip() for line in f.readlines()]


class wordsearch():

    def __init__(self, puzzle_data):

        puzzle_split = []
        for row in puzzle_data:
            puzzle_split.append([letter for letter in row])
        self.puzzle = np.array(puzzle_split)

        self.rows, self.columns = self.puzzle.shape

    def word_search(self, word):

        word = np.array([letter for letter in word])
        L = len(word)

        count = 0

        # Identify every location with the first letter of the target word,
        # then check all directions to find a match with the full target word
        for row, col in zip(*np.where(self.puzzle == word[0])):

            # Construct masks. We need to check eight directions from the first
            # letter, which will be made up of combinations of the following
            # masks:
            row_down = np.arange(row, row+L)
            row_up = np.arange(row-L+1, row+1)[::-1]
            col_right = np.arange(col, col+L)
            col_left = np.arange(col-L+1, col+1)[::-1]

            # Check each direction from the first letter
            for row_mask, col_mask in [
                (row*np.ones(L, dtype=int), col_right),
                (row_down, col_right),
                (row_down, col*np.ones(L, dtype=int)),
                (row_down, col_left),
                (row*np.ones(L, dtype=int), col_left),
                (row_up, col_left),
                (row_up, col*np.ones(L, dtype=int)),
                (row_up, col_right)
            ]:
                # Only consider cases that don't go outside the puzzle
                # dimensions
                if not (
                    np.any(row_mask >= self.rows) or
                    np.any(col_mask >= self.columns)
                ):
                    if not (np.any(row_mask < 0) or np.any(col_mask < 0)):

                        # Count if we match the target word
                        candidate_word = self.puzzle[row_mask, col_mask]
                        if np.all(candidate_word == word):
                            count += 1

        return count

    def crossword_search(self, word):

        word = np.array([letter for letter in word])
        L = len(word)//2

        count = 0

        # We now identify the locations of the middle letter, and then check
        # the two diagonals of the cross for the target word
        for row, col in zip(*np.where(self.puzzle == word[L])):

            # The diagonals of the cross consist of these masks
            diag_row_mask, diag_col_mask = (
                np.arange(row-L, row+L+1),
                np.arange(col-L, col+L+1)
            )

            # Again, don't consider masks which go outside the puzzle
            # dimensions
            if not (
                np.any(diag_row_mask >= self.rows) or
                np.any(diag_col_mask >= self.columns)
            ):
                if not (
                    np.any(diag_row_mask < 0) or
                    np.any(diag_col_mask < 0)
                ):

                    # Get the two diagonals
                    candidate_word_diag_1 = self.puzzle[
                        diag_row_mask, diag_col_mask
                    ]
                    candidate_word_diag_2 = self.puzzle[
                        diag_row_mask, diag_col_mask[::-1]
                    ]

                    # Count the word if both diagonals are equal to the target
                    # word, where the word can be in either direction
                    if (
                        np.all(candidate_word_diag_1 == word) or
                        np.all(candidate_word_diag_1[::-1] == word)
                    ):
                        if (
                            np.all(candidate_word_diag_2 == word) or
                            np.all(candidate_word_diag_2[::-1] == word)
                        ):
                            count += 1

        return count


# Part One
# --------

ws = wordsearch(puzzle_data)
print(ws.word_search('XMAS'))

# Part Two
# --------
print(ws.crossword_search('MAS'))
