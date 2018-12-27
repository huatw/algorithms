class Solution:
    def maxPathSum(self, root):
        def dfs(node):
            if not node:
                return 0, -float('inf')

            (left_sum, left_res), (right_sum, right_res) = dfs(node.left), dfs(node.right)
            cur_res = max(node.val + left_sum + right_sum, left_res, right_res)
            ret_sum = node.val + max(left_sum, right_sum)
            return ret_sum if ret_sum > 0 else 0, cur_res

        return dfs(root)[1]



class Solution:
    def maxPathSum(self, root):
        res = -float('inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum, right_sum = dfs(node.left), dfs(node.right)
            cur_sum = node.val + left_sum + right_sum
            res = max(res, cur_sum)
            ret_sum = node.val + max(left_sum, right_sum)
            return ret_sum if ret_sum > 0 else 0

        dfs(root)
        return res


# follow up, print path inorder
class Solution:
    def maxPathSum(self, root):
        res = -float('inf'), []

        def dfs(node):
            nonlocal res
            if not node:
                return 0, []
            (left_sum, left_path), (right_sum, right_path) = dfs(node.left), dfs(node.right)
            res = max(res, (node.val + left_sum + right_sum, left_path + [node.val] + right_path))
            ret_sum, ret_path = max((left_sum, left_path), (right_sum, right_path))

            return max((0, []), (node.val + ret_sum, [node.val] + ret_path))

        dfs(root)
        return res
