'''
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].

1 1 2 2 3 7
1 2 3 4 5 7
  1 1 2 2
'''
class Solution:
    def minIncrementForUnique(self, nums):
        nums = sorted(nums)

        prev = -float('inf')
        total = 0

        for num in nums:
            if num > prev:
                prev = num
            else:
                total += prev + 1 - num
                prev += 1

        return total