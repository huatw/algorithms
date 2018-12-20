class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit_chs_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(idx, path):
            if idx == len(digits):
                return [''.join(path)]
            res = []
            for ch in digit_chs_map[digits[idx]]:
                path.append(ch)
                res += dfs(idx + 1, path)
                path.pop()
            return res

        return dfs(0, [])


class Solution:
    def letterCombinations(self, digits):
        m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        if len(digits) == 1:
            return list(m[digits])

        arrs = self.letterCombinations(digits[1:])
        return [ch + arr for ch in m[digits[0]] for arr in arrs]

