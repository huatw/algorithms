class Solution:
    def islandPerimeter(self, grid):
        perimeter = 0

        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    perimeter += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
