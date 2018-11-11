'''
Input: [2,3,-2,4]
Output: 6

Input: [-2,0,-1]
Output: 0


max_product_at[-1] = -float('inf')
max_product_at[0] = max(
  max_product_at[i - 1],
  max_product_ends_at[i],
  min_product_ends_at[i],
)
...
max_product_at[i] = max(
  max_product_at[i - 1],
  max_product_ends_at[i],
  min_product_ends_at[i],
)


max_product_ends_at[-1] = 1
min_product_ends_at[-1] = -1
max_product_ends_at[0] = max(
  max_product_ends_at[i - 1] * nums[i],
  min_product_ends_at[i - 1] * nums[i],
  nums[i]
)
....
max_product_ends_at[i] = max(
  max_product_ends_at[i - 1] * nums[i],
  min_product_ends_at[i - 1] * nums[i],
  nums[i]
)
min_product_ends_at[i] = min(
  max_product_ends_at[i - 1] * nums[i],
  min_product_ends_at[i - 1] * nums[i],
  nums[i]
)
'''
class Solution:
    def maxProduct(self, nums):
        max_product_at, max_product_ends_at, min_product_ends_at = -float('inf'), 1, 1

        for num in nums:
            min_product_ends_at, max_product_ends_at = min(max_product_ends_at * num, min_product_ends_at * num, num), max(max_product_ends_at * num, min_product_ends_at * num, num)
            max_product_at = max(max_product_at, min_product_ends_at, max_product_ends_at)

        return max_product_at

class Solution:
    def maxProduct(self, nums):
        max_acc, min_acc = 1, 1
        res = -float('inf')

        for n in nums:
            max_acc, min_acc = max(max_acc * n, min_acc * n, n), min(max_acc * n, min_acc * n, n)
            res = max(res, max_acc, min_acc)

        return res
