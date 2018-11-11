# space O(n)
class Solution:
    def backspaceCompare(self, s, t):
        def parse(chs):
            stack = []
            for ch in chs:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return parse(s) == parse(t)



# space O(1)
class Solution:
    def backspaceCompare(self, s, t):
        i, j = len(s) - 1, len(t) - 1
        cnt_s, cnt_t = 0, 0

        while True:
            while i >= 0 and (cnt_s or s[i] == '#'):
                cnt_s += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (cnt_t or t[j] == '#'):
                cnt_t += 1 if t[j] == '#' else -1
                j -= 1
            if i < 0 or j < 0:
                return i == j
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
