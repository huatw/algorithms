class Solution:
    def tree2str(self, t):
        if not t:
            return ''

        res = str(t.val)

        if t.left and not t.right:
            res += '(' + self.tree2str(t.left) + ')'
        elif not t.left and t.right:
            res += '()(' + self.tree2str(t.right) + ')'
        elif t.left and t.right:
            res += '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'

        return res
