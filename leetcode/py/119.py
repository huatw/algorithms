'''
[1]
[1,1]
[1,2,1]
'''
class Solution:
    def getRow(self, row_index):
        res = [0] * (row_index + 1)
        res[0] = 1
        for level_len in range(1, row_index + 2):
            for i in reversed(range(level_len)):
                res[i] = res[i] + (res[i - 1] if i - 1 >= 0 else 0)
        return res