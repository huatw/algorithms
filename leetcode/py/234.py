# O(n) O(n)
class Solution:
    def isPalindrome(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        lo, hi = 0, len(stack) - 1
        while lo < hi:
            if stack[lo].val != stack[hi].val:
                return False
            lo += 1
            hi -= 1
        return True

# O(n) O(1)
# find middle
# reverse last half
# compare from head/tail to middle
# reverse last half
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



