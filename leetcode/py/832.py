class Solution:
    def flipAndInvertImage(self, grid):
        def flip_invert_row(row):
            row = row[::-1]
            return [1 - num for num in row]

        return [flip_invert_row(row) for row in grid]