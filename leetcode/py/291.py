class Solution:
    def wordPatternMatch(self, pattern, s):
        return self.dfs(pattern, s, {})

    def dfs(self, pattern, s, dct):
        if len(pattern) == 0 and len(s) > 0:
            return False

        if len(pattern) == len(s) == 0:
            return True

        for end in range(1, len(s) - len(pattern) + 2): # +2 because it is the "end of an end"
            if pattern[0] not in dct and s[:end] not in dct.values():
                dct[pattern[0]] = s[:end]
                if self.dfs(pattern[1:], s[end:], dct):
                    return True
                del dct[pattern[0]]
            elif pattern[0] in dct and dct[pattern[0]] == s[:end]:
                if self.dfs(pattern[1:], s[end:], dct):
                    return True

        return False