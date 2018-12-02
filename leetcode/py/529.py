'''
Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''

class Solution:
    def updateBoard(self, board, click):
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        ROW, COL = len(board), len(board[0])
        def is_inside(row, col):
            return 0 <= row < ROW and 0 <= col < COL
        row, col = click
        if is_inside(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + c][col + r] == 'M' for c, r in DIRECTIONS if is_inside(row + c, col + r)])
                if n:
                    board[row][col] = str(n)
                else:
                    board[row][col] = 'B'
                    for r, c in DIRECTIONS:
                        self.updateBoard(board, [row + r, col + c])
        return board
