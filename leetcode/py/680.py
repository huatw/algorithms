'''
Input: "abca"
Output: True
"abc"
'''
class Solution:
    def validPalindrome(self, s):
        def is_p(i, j):
            for k in range(i, j):
                if s[k] != s[j - (k - i)]:
                    return False
            return True

        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return is_p(i, len(s) - i - 2) or is_p(i + 1, len(s) - i - 1)

        return True