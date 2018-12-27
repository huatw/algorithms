class Solution:
    def reverse(self, x):
        res = 0
        op = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            x, digit = divmod(x, 10)
            res = res * 10 + digit
        res *= op
        if 2 ** 31 - 1 >= res >= -(2 ** 31):
            return res
        return 0
