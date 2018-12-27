class Solution(object):
    def hasCycle(self, head):
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False