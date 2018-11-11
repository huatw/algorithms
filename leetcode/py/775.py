'''
Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

    2 1 0
idx 0 1 2
global n2
local n
'''

class Solution:
    def isIdealPermutation(self, nums):
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
        return True