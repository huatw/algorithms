# naive one
class Solution:
    def addTwoNumbers(self, l1, l2):
        str1, str2 = [], []

        while l1:
            str1.append(l1.val)
            l1 = l1.next

        while l2:
            str2.append(l2.val)
            l2 = l2.next

        len1, len2 = len(str1), len(str2)
        if len1 < len2:
            str1 = [0] * (len2 - len1) + str1
        if len1 > len2:
            str2 = [0] * (len1 - len2) + str2

        tenth = 0
        ret = None
        for i in range(1, max(len1, len2) + 1):
            digit = str1[-i] + str2[-i] + tenth
            tenth = digit // 10
            digit = digit % 10

            node = ListNode(digit)
            node.next = ret
            ret = node

        if tenth:
            node = ListNode(tenth)
            node.next = ret
            ret = node

        return ret