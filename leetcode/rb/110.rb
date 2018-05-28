# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
  recur(root)[0]
end

def recur(root)
  return [true, 0] if !root

  is_balanced, h_left = recur(root.left)
  return [false, nil] if !is_balanced

  is_balanced, h_right = recur(root.right)
  return [false, nil] if !is_balanced

  is_balanced = (h_right - h_left).abs <= 1
  return [is_balanced, [h_left, h_right].max + 1]
end



# raise error
def assert(tree)
  return 0 if not tree

  left, right = assert(tree.left), assert(tree.right)
  (left - right).abs > 1 ? raise : 1 + [left, right].max
end

def is_balanced(root)
  assert(root) && true rescue false
end
