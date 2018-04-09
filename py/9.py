class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        return int(str(x)[::-1]) == x




class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1

        while x >= ranger * 10:
            ranger *= 10

        while x:
            left, right = x // ranger, x % 10
            if left != right:
                return False
            x = (x % ranger) // 10
            ranger //= 100

        return True
