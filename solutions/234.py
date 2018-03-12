class Solution:
    def isPalindrome(self, head):
        prev, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp

        if fast:
            slow = slow.next

        while prev and slow:
            if prev.val == slow.val:
                prev, slow = prev.next, slow.next
            else:
                return False

        return True



