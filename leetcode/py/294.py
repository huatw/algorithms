'''
can_win("++++++") = !can_win("--++++") or !can_win("+--+++") ...
can_win(s) => not can_win(next_s) or not can_win(next_s)
'''
class Solution:
    def canWin(self, s):
        cache = {}
        def recur(s):
            if s not in cache:
                cache[s] = False
                for i, (ch1, ch2) in enumerate(zip(s, s[1:])):
                    if ch1 + ch2 == '++' and not recur(s[:i] + '--' + s[i + 2:]):
                        cache[s] = True
                        break
            return cache[s]

        return recur(s)



class Solution:
    def canWin(self, s):
        cache = {}

        def dfs(s):
            if s in cache:
                return cache[s]

            for i, (ch1, ch2) in enumerate(zip(s, s[1:])):
                if ch1 == ch2 == '+' and not dfs(s[:i] + '--' + s[i + 2:]):
                    cache[s] = True
                    return True

            cache[s] = False
            return False

        return dfs(s)
