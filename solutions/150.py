class Solution:
    def evalRPN(self, tokens):
        stack = []
        op = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: y - x,
            '*': lambda x,y: x * y,
            '/': lambda x,y: int(y / x)
        }

        for token in tokens:
            if token in op:
                stack.append(op[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[-1]

