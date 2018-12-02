class Solution:
    def slidingPuzzle(self, board):
        MOVES = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [3, 1, 5], [2, 4]]
        start = ''.join([str(ch) for row in board for ch in row])
        seen = set([start])
        q = collections.deque([(start, start.index('0'), 0)])
        while q:
            board, idx0, steps = q.popleft()
            if board == '123450':
                return steps
            for move in MOVES[idx0]:
                newboard = list(board)
                newboard[move], newboard[idx0] = newboard[idx0], newboard[move]
                newboard = ''.join(newboard)
                if newboard not in seen:
                    seen.add(newboard)
                    q.append((newboard, move, steps + 1))
        return -1



'''
0 1 2
3 4 5
6 7 8
'''
def slidingPuzzle(board):
    MOVES = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
    start = ''.join([str(ch) for row in board for ch in row])
    seen = set([start])
    q = collections.deque([(start, start.index('0'), 0)])
    while q:
        board, idx0, steps = q.popleft()
        if board == '123456780':
            return steps
        for move in MOVES[idx0]:
            newboard = list(board)
            newboard[move], newboard[idx0] = newboard[idx0], newboard[move]
            newboard = ''.join(newboard)
            if newboard not in seen:
                seen.add(newboard)
                q.append((newboard, move, steps + 1))
    return -1
