class MinStack:
    def __init__(self):
        self.my_stack = []

    def push(self, x):
        if not self.my_stack:
            self.my_stack.append((x, x))
        else:
            minimum = self.my_stack[-1][1]
            self.my_stack.append((x, min(x, minimum)))

    def pop(self):
        return self.my_stack.pop()[0]

    def top(self):
        return self.my_stack[-1][0]

    def getMin(self):
        return self.my_stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()