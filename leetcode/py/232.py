"""
list:                   queue
pop back O(1)           pop front O(1)??
push back O(1)          push back O(1)
peek front&back O(1)    peek front O(1)
is empty O(1)           is empty O(1)

[1,2,3,4,5,6]  [1]        []              [7, 8, 9, 10]   [7, 8, 9, 10]
               6 5 4 3 2  [6, 5, 4, 3, 2] [6, 5, 4, 3, 2] []
"""
class MyQueue:
    def __init__(self):
        self.stack = []
        self.rev_stack = []

    def push(self, x): # push back
        self.stack.append(x)

    def move(self):
        if not self.rev_stack:
            while self.stack:
                self.rev_stack.append(self.stack.pop())

    def pop(self): # pop front
        self.move()
        return self.rev_stack.pop()

    def peek(self): # peek front
        self.move()
        return self.rev_stack[-1]

    def empty(self): # is empty
        return len(self.stack) + len(self.rev_stack) == 0




# double stack
class MyQueue:
    def __init__(self):
        self.q = []
        self.rev_q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        self.move()
        return self.rev_q.pop()

    def peek(self):
        self.move()
        return self.rev_q[-1]

    def empty(self):
        return not self.rev_q and not self.q

    def move(self):
        if not self.rev_q:
            while self.q:
                self.rev_q.append(self.q.pop())


# naive
class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        first, *self.q = self.q
        return first

    def peek(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()