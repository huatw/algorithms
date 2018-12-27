# O(n) O(n)
class Solution:
    def isPalindrome(self, head):
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        return all(n1 == n2 for n1, n2 in zip(stack, stack[::-1]))


# O(n) O(1)
class Solution:
    def isPalindrome(self, head):
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev, slow.next, slow, fast = slow, prev, slow.next, fast.next.next

        if fast:
            slow = slow.next

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev, slow = prev.next, slow.next

        return True
