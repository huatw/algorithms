# n * (k ** n)
class Solution:
    def crackSafe(self, n, k):
        res = []
        seen = set()
        def dfs(prefix):
            for digit in map(str, reversed(range(k))):
                s = prefix + digit
                if s not in seen:
                    seen.add(s)
                    res.append(digit)
                    dfs(s[1:])

        dfs('0' * (n - 1))
        return '0' * (n - 1) + ''.join(res)


# n * (k ** n)
class Solution:
    def crackSafe(self, n, k):
        res = '0' * (n - 1)
        seen = set()
        for _ in range(k ** n):
            prefix = res[-n + 1:] if n > 1 else ''
            for num in reversed(range(k)):
                s = prefix + str(num)
                if s not in seen:
                    seen.add(s)
                    res += str(num)
                    break
        return res


# k ** n
class Solution:
    def crackSafe(self, n, k):
        M = k ** (n - 1)
        P = [q * k + i for i in range(k) for q in range(M)]
        ans = []

        for i in range(k ** n):
            j = i
            while P[j] >= 0:
                ans.append(str(j / M))
                P[j], j = -1, P[j]

        return ''.join(ans) + '0' * (n - 1)
