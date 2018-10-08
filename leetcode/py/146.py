# DoubleLinkedList & Map
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.dummy_head = ListNode(None, None)
        self.dummy_end = ListNode(None, None)
        self.dummy_head.next = self.dummy_end
        self.dummy_end.prev = self.dummy_head

    def move_to_first(self, node):
        # 1. remove node from list
        prev_node, next_node = node.prev, node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        # 2. attach to head
        dummy_next = self.dummy_head.next
        self.dummy_head.next = node
        dummy_next.prev = node
        node.next = dummy_next
        node.prev = self.dummy_head

    def remove_last(self):
        prev_node, node = self.dummy_end.prev.prev, self.dummy_end.prev
        node.next = None
        node.prev = None
        self.d.pop(node.key)
        prev_node.next = self.dummy_end
        self.dummy_end.prev = prev_node

    def get(self, key):
        if key not in self.d:
            return -1
        # update linkedlist
        self.move_to_first(self.d[key])
        return self.d[key].val

    def set(self, key, val):
        if key not in self.d:
            # insert
            if self.capacity == len(self.d):
                # remove last and insert
                self.remove_last()
            self.d[key] = Node(key, val)
        else:
            # update
            self.d[key].val = val
        self.move_to_first(self.d[key])


# orderedDict
import collections

class LRUCache:
    def __init__(self, capacity):
        self.d = collections.OrderedDict()
        self.capacity = capacity

    def touch(self, key):
        self.d.move_to_end(key)
        return self.d[key]

    def get(self, key):
        if key not in self.d:
            return -1
        return self.touch(key)

    def set(self, key, value):
        # insert
        # remove least recently used
        if len(self.d) == self.capacity and key not in self.d:
            self.d.popitem(last=False)

        self.d[key] = value
        self.touch(key)

