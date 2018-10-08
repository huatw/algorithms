class Solution:
    def addDigits(self, num):
        while num // 10 > 0:
            res = 0
            while num // 10 > 0:
                num, digit = divmod(num, 10)
                res += digit
            num += res

        return num


class Solution(object):
    def addDigits(self, num):
        return 0 if num == 0 else (num - 1) % 9 + 1