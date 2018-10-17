# recur nlogn
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return
        idx = nums.index(max(nums))
        ret = TreeNode(nums[idx])
        ret.left = self.constructMaximumBinaryTree(nums[:idx])
        ret.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return ret
