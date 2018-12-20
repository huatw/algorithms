'''
x^n
(x^2)^(n/2)
x (x^2)^((n - 1)/2)
'''
class Solution:
    def myPow(self, x, n):
        m = abs(n)
        res = 1
        while m:
            if m % 2 == 0:
                x *= x
                m /= 2
            else:
                res *= x
                x *= x
                m = (m - 1) / 2
        return res if n > 0 else 1 / res

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
