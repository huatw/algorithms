"""
queue                stack
peek front O(1)      top back O(1)
pop front O(1)       pop back O(1)
append back O(1)     append back O(1)
is empty O(1)        is empty O(1)

[1, 2, 3, 4, 5]   [5]          [1, 2, 3, 4]
                  [1, 2, 3, 4] []
"""
# naive
class MyStack:
    # O(1)
    def __init__(self):
        self.q = collections.deque()

    # O(1)
    def push(self, x):
        self.q.append(x)

    # O(n)
    def pop(self):
        self.q.rotate()
        return self.q.popleft()

    # O(n) problem here
    def top(self):
        self.q.rotate()
        val = self.q.popleft()
        self.q.append(val)
        return val

    # O(1)
    def empty(self):
        return len(self.q) == 0



class MyStack:
    # O(1)
    def __init__(self):
        self.q = collections.deque()

    # O(n) # eager rotate q
    def push(self, x):
        self.q.append(x)
        self.q.rotate()

    # O(1)
    def pop(self):
        return self.q.popleft()

    # O(1)
    def top(self):
        return self.q[0]

    # O(1)
    def empty(self):
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()