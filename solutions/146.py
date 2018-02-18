# 100%
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.dict:
            return -1

        node = self.dict[key]
        if self.head.next.key != key:
            self.deleteNode(node)
            self.insertHead(node)

        return node.value

    def put(self, key, value):
        # update value
        if key in self.dict:
            if self.dict[key].value != value:
                self.dict[key].value = value
            self.get(key)
            return
        # insert new Node
        node = Node(key, value)
        self.dict[key] = node
        self.insertHead(node)

        if self.size < self.capacity:
            self.size += 1
        # delete tail node
        else:
            self.dict.pop(self.tail.prev.key)
            self.deleteNode(self.tail.prev)


# orderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key):
        if key not in self.d:
            return -1

        value = self.d[key] # value = self.d.pop(key)
        del self.d[key]     ### pop is slower...
        self.d[key] = value
        return value

    def put(self, key, value):
        if key in self.d:
            del self.d[key] # self.d.pop(key)
        elif len(self.d) == self.capacity:
            self.d.popitem(last=False)

        self.d[key] = value
