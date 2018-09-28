class Solution:
    def myPow(self, x, n):
        m = abs(n)
        ans = 1.0

        while m:
            if m % 2:
                ans *= x
            x *= x
            m //= 2

        return ans if n >= 0 else 1 / ans
