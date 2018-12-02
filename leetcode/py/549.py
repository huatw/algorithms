# O(n) post order
class Solution:
    def longestConsecutive(self, root):
        def post_order_traversal(node: TreeNode) -> (int, int):
            if not node:
                return (0, 0, 0)

            inc, dec = 1, 1
            left_inc, left_dec, left_max = post_order_traversal(node.left)
            right_inc, right_dec, right_max = post_order_traversal(node.right)

            if left_inc and node.left.val == node.val + 1:
                inc = max(inc, left_inc + 1)
            if left_dec and node.left.val == node.val - 1:
                dec = max(dec, left_dec + 1)
            if right_inc and node.right.val == node.val + 1:
                inc = max(inc, right_inc + 1)
            if right_dec and node.right.val == node.val - 1:
                dec = max(dec, right_dec + 1)

            cur_max = inc + dec - 1
            return (inc, dec, max(left_max, right_max, cur_max))

        return post_order_traversal(root)[2]
