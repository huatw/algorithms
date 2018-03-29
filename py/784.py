class Solution:
    def letterCasePermutation(self, S):
        self.res = []
        arr = [[ch] if ch.isdigit() else [ch.upper(), ch.lower()] for ch in S]
        self.recur(arr)
        return self.res

    def recur(self, rest, acc = ''):
        if not rest:
            self.res.append(acc)
            return

        for ch in rest[0]:
            self.recur(rest[1:], acc + ch)