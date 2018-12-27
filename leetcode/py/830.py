class Solution:
    def largeGroupPositions(self, s):
        res = []
        token, cnt = '', 0
        for i, ch in enumerate(s):
            if ch == token:
                cnt += 1
            else:
                if cnt >= 3:
                    res.append([i - cnt, i - 1])
                token = ch
                cnt = 1

        if cnt >= 3:
            res.append([i - cnt + 1, i])
        return res