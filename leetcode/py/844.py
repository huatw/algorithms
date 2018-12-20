# space O(1)
class Solution:
    def backspaceCompare(self, s, t):
        idx_s, idx_t = len(s) - 1, len(t) - 1
        cnt_s, cnt_t = 0, 0
        while True:
            while idx_s >= 0 and (s[idx_s] == '#' or cnt_s > 0):
                cnt_s += 1 if s[idx_s] == '#' else -1
                idx_s -= 1
            while idx_t >= 0 and (t[idx_t] == '#' or cnt_t > 0):
                cnt_t += 1 if t[idx_t] == '#' else -1
                idx_t -= 1
            ch_s, ch_t = s[idx_s] if idx_s >= 0 else None, t[idx_t] if idx_t >= 0 else None
            if ch_s != ch_t:
                return False
            if ch_s == ch_t == None:
                return True
            idx_s, idx_t = idx_s - 1, idx_t - 1



class Solution:
    def backspaceCompare(self, s1, s2):
        def trans_state(s, idx, cnt):
            while idx >= 0 and (s[idx] == '#' or cnt > 0):
                cnt += 1 if s[idx] == '#' else -1
                idx -= 1
            ch = s[idx] if idx >= 0 else None
            idx -= 1
            return (ch, s, idx, cnt)
        state1, state2 = (s1, len(s1) - 1, 0), (s2, len(s2) - 1, 0)
        while True:
            ch1, *state1 = trans_state(*state1)
            ch2, *state2 = trans_state(*state2)
            if ch1 != ch2:
                return False
            if ch1 == ch2 == None:
                return True


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
