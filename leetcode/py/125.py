class Solution:
    def isPalindrome(self, s):
        lo, hi = 0, len(s) - 1

        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
            elif not s[hi].isalnum():
                hi -= 1
            else:
                if s[lo].lower() != s[hi].lower():
                    return False
                lo += 1
                hi -= 1
        return True
