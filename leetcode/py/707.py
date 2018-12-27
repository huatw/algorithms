class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.len = 0

    def debug(self):
        cur = self.head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res, self.head.val, self.tail.val)

    def get(self, index):
        if index >= self.len:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        self.len += 1
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head

    def addAtTail(self, val):
        self.len += 1
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = new_tail

    def addAtIndex(self, index, val):
        if index > self.len:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            self.len += 1
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            next_node = prev_node.next
            prev_node.next = Node(val)
            prev_node.next.next = next_node

    def deleteAtIndex(self, index):
        if index > self.len - 1:
            return
        self.len -= 1
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            prev_node.next = prev_node.next.next
            if index == self.len:
                self.tail = prev_node
