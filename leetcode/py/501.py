# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findMode(self, root):
        val_cnt_map = collections.defaultdict(int)
        def recur(node):
            if not node:
                return
            val_cnt_map[node.val] += 1
            recur(node.left)
            recur(node.right)
        recur(root)
        res = []
        max_cnt = 0
        for val, cnt in val_cnt_map.items():
            if cnt > max_cnt:
                max_cnt = cnt
                res = [val]
            elif cnt == max_cnt:
                res.append(val)
        return res



class Solution:
    def findMode(self, root):
        self.res_val = []
        self.res_cnt = 0
        self.cur_val = None
        self.cur_cnt = 0
        def update(val):
            if self.cur_cnt > self.res_cnt:
                self.res_cnt = self.cur_cnt
                self.res_val = [self.cur_val]
            elif self.cur_cnt == self.res_cnt and self.cur_val:
                self.res_val.append(self.cur_val)
            self.cur_val = val
            self.cur_cnt = 1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if node.val == self.cur_val:
                self.cur_cnt += 1
            else:
                update(node.val)
            inorder(node.right)
        inorder(root)
        update(None)
        return self.res_val
