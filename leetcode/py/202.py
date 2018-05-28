class Solution:
    def isHappy(self, n):
        met = set([n])

        while n != 1:
            n = sum([int(ch) * int(ch) for ch in str(n)])
            if n in met:
                return False
            met.add(n)

        return True



