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