# On2
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(None)
        dummy.next = head

        cur = head
        while cur and cur.next:
            nextNode = cur.next
            if nextNode.val < cur.val:
                cur.next = nextNode.next
                pnode = dummy
                while nextNode.val > pnode.next.val:
                    pnode = pnode.next
                nextNode.next = pnode.next
                pnode.next = nextNode
            else:
                cur = nextNode

        return dummy.next



