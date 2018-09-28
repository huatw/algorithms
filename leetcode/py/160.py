# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# m+n trick
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return

        a, b = headA, headB
        cnt = 0

        while a != b and cnt < 3:
            a = a.next
            b = b.next
            if not a:
                a = headB
                cnt += 1
            if not b:
                b = headA
                cnt += 1

        if a == b:
            return


# m+n
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def get_list_len(root):
            l = 0

            while root:
                root = root.next
                l += 1

            return l

        a_len = get_list_len(headA)
        b_len = get_list_len(headB)

        if a_len > b_len:
            while a_len > b_len:
                headA = headA.next
                a_len -= 1
        else:
            while a_len < b_len:
                headB = headB.next
                b_len -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
