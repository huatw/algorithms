class Solution:
    def generatePossibleNextMoves(self, s):
        res = []
        for i, (ch1, ch2) in enumerate(zip(s, s[1:])):
            if ch1 + ch2 == '++':
                res.append(s[:i] + '--' + s[i + 2:])
        return res

class Solution:
    def generatePossibleNextMoves(self, s):
        res = []

        for i, (ch1, ch2) in enumerate(zip(s, s[1:])):
            if ch1 == ch2 == '+':
                res.append(s[:i] + '--' + s[i + 2:])

        return res