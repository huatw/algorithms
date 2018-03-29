# DP
class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        res = [1, 1] # add one more for s[2]

        for i in range(1, len(s)):
            if s[i] == '0':
                if 0 < int(s[i-1:i+1]) <= 26:
                    res.append(res[i-1])
                else:
                    return 0
            else:
                if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                    res.append(res[i] + res[i-1])
                else:
                    res.append(res[i])

        return res[-1]


















