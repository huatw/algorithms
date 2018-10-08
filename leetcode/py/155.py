'''
stack [2, 4, 1, 5, 3]
min   [2, 2, 1, 1, 1]
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))

    def pop(self):
        self.min.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()