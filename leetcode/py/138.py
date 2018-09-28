# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# using map
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return

        cur = head
        node_map = {}

        while cur:
            node_map[cur] = RandomListNode(cur.label)
            cur = cur.next

        cur = head
        while cur:
            node_map[cur].next = node_map[cur.next] if cur.next in node_map else None
            node_map[cur].random = node_map[cur.random] if cur.random in node_map else None
            cur = cur.next

        return node_map[head]


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head

        p = head
        # insert copied node
        while p:
            temp = p.next
            p_copy = RandomListNode(p.label)
            p.next = p_copy
            p_copy.next = temp
            p = temp

        p = head
        ret = p.next

        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        p = head

        while p:
            temp = p.next.next
            if temp:
                p.next.next = temp.next
            p.next = temp
            p = temp

        return ret

        #### !!! error, previous pointer is nolonger ordered
        # while p:
        #     temp = p.next.next
        #     if p.random:
        #         p.next.random = p.random.next
        #     if temp:
        #         p.next.next = temp.next
        #     # point to original one
        #     p.next = temp
        #     p = temp
