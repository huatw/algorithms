class Solution:
    def reverse(self, x):
        res = 0
        minus = -1 if x < 0 else 1
        x = minus * x

        while x != 0:
            x, digit = divmod(x, 10)
            res = res * 10 + digit

        res *= minus
        if 2 ** 31 - 1 >= res >= -(2 ** 31):
            return res
        return 0