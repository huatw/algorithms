'''
Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

'''
class Solution:
    def calculate(self, s):
        # " 3+5 / 2 " => ['3', '+', '5', '/', '2']
        def tokenize(s):
            tokens = []
            token = ''
            for ch in s:
                if ch == '+' or ch == '-' or ch == '*' or ch == '/':
                    if token:
                        tokens.append(token)
                        token = ''
                    tokens.append(ch)
                elif ch != ' ':
                    token += ch
            if token:
                tokens.append(token)
            return tokens

        # ['3', '+', '5', '/', '2'] => ['3', '+', ['5', '/', '2']]
        def parse(tokens):
            stacks = [[]]
            should_pop = False
            for token in tokens:
                if should_pop:
                    should_pop = False
                    sub_stack = stacks.pop()
                    sub_stack.append(token)
                    stacks[-1].append(sub_stack)
                elif token == '*' or token == '/':
                    should_pop = True
                    stacks.append([stacks[-1].pop(), token])
                else:
                    stacks[-1].append(token)
            return stacks[-1]

        def eval_val(ast):
            def get_val(node):
                if not isinstance(node, list):
                    return int(node)
                left, op, right = node
                if op == '*':
                    return get_val(left) * get_val(right)
                if op == '/':
                    return get_val(left) // get_val(right)

            total = get_val(ast[0])
            while len(ast) > 1:
                right = get_val(ast.pop())
                op = ast.pop()
                if op == '+':
                    total += right
                elif op == '-':
                    total -= right
            return total

        tokens = tokenize(s)
        ast = parse(tokens)
        val = eval_val(ast)

        return val



class Solution:
    def calculate(self, s):
        tokens = []
        token = ''
        for ch in s:
            if ch == ' ':
                pass
            elif ch.isdigit():
                token += ch
            else:
                tokens.append(token)
                token = ''
                tokens.append(ch)
        tokens.append(token)

        stack = []
        should_pop = False
        for token in tokens:
            if should_pop:
                should_pop = False
                second = int(token)
                op = stack.pop()
                first = int(stack.pop())
                if op == '*':
                    stack.append(first * second)
                elif op == '/':
                    stack.append(first // second)
            else:
                if token == '*' or token == '/':
                    should_pop = True
                stack.append(token)

        tokens = stack
        stack = []
        should_pop = False
        for token in tokens:
            if should_pop:
                should_pop = False
                second = int(token)
                op = stack.pop()
                first = int(stack.pop())
                if op == '+':
                    stack.append(first + second)
                elif op == '-':
                    stack.append(first - second)
            else:
                if token == '+' or token == '-':
                    should_pop = True
                stack.append(token)

        return int(stack[-1])

