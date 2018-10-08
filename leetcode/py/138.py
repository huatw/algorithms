# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# map one pass
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return

        node_map = collections.defaultdict(lambda: None)
        cur = head
        while cur:
            if cur not in node_map:
                node_map[cur] = RandomListNode(cur.label)
            if cur.next and cur.next not in node_map:
                node_map[cur.next] = RandomListNode(cur.next.label)
            if cur.random and cur.random not in node_map:
                node_map[cur.random] = RandomListNode(cur.random.label)
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next

        return node_map[head]


# map two pass
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return

        node_map = collections.defaultdict(lambda: None)
        cur = head
        while cur:
            node_map[cur] = RandomListNode(cur.label)
            cur = cur.next

        cur = head
        while cur:
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next

        return node_map[head]






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
