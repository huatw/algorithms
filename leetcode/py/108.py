class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return

        mid = math.floor(len(nums) / 2)

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node



