'''
Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

["(","1","+","(","4","+","5","+","2",")","-","3",")","+","(","6","+","8",")"]

'''
class Solution:
    def calculate(self, s):
        # 2-(1+2) => ['2', '-', '(', '1', '+', '2', ')']
        def tokenize(s):
            tokens = []
            token = ''
            for ch in s:
                if ch == '+' or ch == '-' or ch == '(' or ch == ')':
                    if token:
                        tokens.append(token)
                        token = ''
                    tokens.append(ch)
                elif ch != ' ':
                    token += ch
            if token:
                tokens.append(token)
            return tokens

        # ['2', '-', '(', '1', '+', '2', ')'] => [2, -, [1, +, 2]]
        def parse(tokens):
            stacks = [[]]
            for token in tokens:
                if token == '(':
                    stacks.append([])
                elif token == ')':
                    sub_stack = stacks.pop()
                    stacks[-1].append(sub_stack)
                else:
                    stacks[-1].append(token)
            return stacks[-1]

        def eval_val(ast):
            def get_val(node):
                return eval_val(node) if isinstance(node, list) else int(node)

            total = get_val(ast[0])
            while len(ast) > 1:
                right = get_val(ast.pop())
                op = ast.pop()
                if op == '+':
                    total += right
                if op == '-':
                    total -= right
            return total

        # def eval_val(ast):
        #     if not isinstance(ast, list):
        #         return int(ast)
        #     if len(ast) == 1:
        #         return eval_val(ast[0])
        #     left, op, right, *rest = ast
        #     if op == '+':
        #         val = eval_val(left) + eval_val(right)
        #     if op == '-':
        #         val = eval_val(left) - eval_val(right)

        #     return eval_val([val] + rest)

        tokens = tokenize(s)
        ast = parse(tokens)
        val = eval_val(ast)

        return val



class Solution:
    def calculate(self, s):
        tokens = []
        token = ''

        for ch in s + '$':
            if ch == ' ':
                pass
            elif ch.isdigit():
                token += ch
            else:
                if token:
                    tokens.append(token)
                    token = ''
                tokens.append(ch)

        stack = []
        for token in (['('] + tokens + [')'])[::-1]:
            if token == '(':
                # pop stack
                total = int(stack.pop())
                while stack[-1] != ')':
                    op = stack.pop()
                    n = int(stack.pop())
                    if op == '+':
                        total += n
                    elif op == '-':
                        total -= n
                stack.pop()
                stack.append(total)
            else:
                stack.append(token)

        return stack[-1]




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
                if token:
                    tokens.append(token)
                    token = ''
                tokens.append(ch)
        if token:
            tokens.append(token)

        def eval_level(stack):
            stack.pop() # ')'
            total = 0
            while stack[-2] != '(':
                second = int(stack.pop())
                op = stack.pop()
                if op == '+':
                    total += second
                if op == '-':
                    total -= second
            total += int(stack.pop())
            stack.pop() # '('
            return total

        stack = []
        should_pop = False
        for token in ['('] + tokens + [')']:
            if should_pop:
                should_pop = False
                stack.append(eval_level(stack))
            if token == ')':
                should_pop = True
            stack.append(token)

        return eval_level(stack)
