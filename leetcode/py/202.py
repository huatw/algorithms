class Solution:
    def isHappy(self, n):
        seen = set([n])

        while n != 1:
            n = sum(int(ch) ** 2 for ch in str(n))
            if n in seen:
                return False
            seen.add(n)

        return True
