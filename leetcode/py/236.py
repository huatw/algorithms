'''
       _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
'''
# post order?
post (root, p, q) {
      if (!root) {
        return
      }
      const arr = []
      const stack = [[root, false]]
      while (stack.length > 0) {
        const [node, isSeen] = stack.pop()
        if (isSeen) {
          arr.push(node.val)
        } else {
          stack.push([node, true])
          if (node.right) {
            stack.push([node.right, false])
          }
          if (node.left) {
            stack.push([node.left, false])
          }
        }
      }
      return arr
    }
  }
class Solution:
    def lowestCommonAncestor(self, root, p, q):


# use map to memo
def lowestCommonAncestor(self, root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root

        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right



