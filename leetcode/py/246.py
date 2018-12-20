class Solution:
    def isStrobogrammatic(self, num):
        digit_map = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0'
        }

        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if num[lo] not in digit_map or digit_map[num[lo]] != num[hi]:
                return False
            lo += 1
            hi -= 1
        return True

