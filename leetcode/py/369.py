# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        dummy = ListNode(0)
        dummy.next = head

        def recur(node):
            add_val = recur(node.next) if node.next else 1
            tenth, node.val = divmod(node.val + add_val, 10)
            return tenth

        recur(dummy)
        return dummy.next if dummy.val == 0 else dummy