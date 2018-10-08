"""
vertical order => element array with same diff are always append top down
               => level order traverse to ensure top down
"""
import queue
import collections
class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        v_level_dict = collections.defaultdict(list)
        q = queue.deque([(root, 0)])

        while q:
            node, v_level = q.popleft()
            if node:
                v_level_dict[v_level].append(node.val)
                q.append((node.left, v_level - 1))
                q.append((node.right, v_level + 1))

        level_range = v_level_dict.keys()
        res = [v_level_dict[i] for i in range(min(level_range), max(level_range) + 1)]

        return res

