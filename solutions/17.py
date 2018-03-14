class Solution:
    def letterCombinations(self, digits):
        m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        if len(digits) == 1:
            return list(m[digits])

        arrs = self.letterCombinations(digits[1:])
        return [ch + arr for ch in m[digits[0]] for arr in arrs]

