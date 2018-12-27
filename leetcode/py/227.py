class Solution:
    def calculate(self, s):
        def tokenize(s):
            tokens = []
            token = ''
            for ch in s:
                if ch == ' ':
                    continue
                elif ch in '+-*/':
                    if token:
                        tokens.append(token)
                        token = ''
                    tokens.append(ch)
                else:
                    token += ch
            if token:
                tokens.append(token)
            return tokens

        def parse(tokens):
            stack = []
            should_pop = False
            for token in tokens:
                if should_pop:
                    should_pop = False
                    op = stack.pop()
                    left = stack.pop()
                    stack.append([left, op, token])
                else:
                    if token in '*/':
                        should_pop = True
                    stack.append(token)
            return stack

        def get_val(var):
            return evaluate(var) if isinstance(var, list) else int(var)

        def evaluate(ast):
            total = get_val(ast[0])
            for i in range(1, len(ast), 2):
                op, val = ast[i], get_val(ast[i + 1])
                if op == '+':
                    total += val
                elif op == '-':
                    total -= val
                elif op == '*':
                    total *= val
                elif op == '/':
                    total //= val
            return total

        tokens = tokenize(s)
        ast = parse(tokens)
        res = evaluate(ast)
        return res
