class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        res = self.head
        cur = self.head
        idx = 1

        while cur:
            if random.randint(1, idx) == 1:
                res = cur.val
            cur = cur.next
            idx += 1

        return res
