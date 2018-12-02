# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        cur = dummy

        hq = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(hq)

        while hq:
            val, i, node = heapq.heappop(hq)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(hq, (node.next.val, i, node.next))
        return dummy.next


# divde : py exceed maximum recursion. js can pass
class Solution:
    def mergeKLists(self, lists):
        start, end = 0, len(lists) - 1
        return self.divideLists(lists, start, end)


    def divideMerge(self, lists, start, end):
        if start >= end:
            return lists[start]

        mid = (start + end) // 2
        l1 = self.divideMerge(lists, start, mid)
        l2 = self.divideMerge(lists, mid + 1, end)
        return self.merge(l1, l2)


    def merge(self, l1, l2):
        if l1 === None: return l2
        if l2 === None: return l1

        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1

        l2.next = self.merge(l2.next, l1)
        return l2




# change to loop
class Solution:
    def mergeKLists(self, lists):
        if not Lists: return None
        start, end = 0, len(lists) - 1
        return self.divideMerge(lists, start, end)


    def divideMerge(self, lists, start, end):
        if start >= end:
            return lists[start]

        mid = (start + end) // 2
        l1 = self.divideMerge(lists, start, mid)
        l2 = self.divideMerge(lists, mid + 1, end)
        return self.merge(l1, l2)


    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return head.next



# priority q
class Solution:
    def mergeKLists(self, lists):
        current = sentinel = ListNode(0)
        lists = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(lists)
        while lists:
            _, i, node = heapq.heappop(lists)
            current.next = node
            current = current.next
            nextNode = node.next
            if nextNode:
                heapq.heappush(lists, (nextNode.val, i, nextNode))
        return sentinel.next



# 40%
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()

        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))

        while q.qsize():
            _, i, node = q.get()
            curr.next = node
            curr = curr.next
            if node.next:
                q.put((node.next.val, i, node.next))
        return dummy.next
