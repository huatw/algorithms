class Solution:
    def rotatedDigits(self, N):
        res = 0
        for x in range(1, N + 1):
            S = str(x)
            if all(d not in '347' for d in S) and any(d in '2569' for d in S):
                res += 1
        return res

class Solution:
    def rotatedDigits(self, N):
        def with_cache(fn):
            cache = {}
            def wrapper(i, equality_flag, involution_flag):
                if (i, equality_flag, involution_flag) not in cache:
                    cache[(i, equality_flag, involution_flag)] = fn(i, equality_flag, involution_flag)
                return cache[(i, equality_flag, involution_flag)]
            return wrapper

        A = list(map(int, str(N)))

        def dfs(i, equality_flag, involution_flag):
            if i == len(A):
                return +(involution_flag)
            return sum(dfs(i+1, equality_flag and d == A[i], involution_flag or d in {2, 5, 6, 9}) \
                for d in range(A[i] + 1 if equality_flag else 10) if d not in {3, 4, 7})

        return dfs(0, True, False)
