class Solution:
    def isStrobogrammatic(self, num):
        digit_map = {
            '1': '1',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }
        res = []
        for digit in num:
            if digit not in digit_map:
                return False
            res.append(digit_map[digit])
        return ''.join(res[::-1]) == num

class Solution:
    def isStrobogrammatic(self, num):
        digit_map = {
            '1': '1',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if not (num[lo] in digit_map and num[hi] in digit_map and digit_map[num[lo]] == num[hi]):
                return False
            lo += 1
            hi -= 1

        return True
