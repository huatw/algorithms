# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        dummy = ListNode(None)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        ret = TreeNode(slow.next.val)
        ret.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        ret.left = self.sortedListToBST(head)

        return ret


