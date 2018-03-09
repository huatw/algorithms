class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        ret = head.next
        head.next, ret.next = self.swapPairs(ret.next), head

        return ret
