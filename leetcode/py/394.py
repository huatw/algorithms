class Solution:
    def decodeString(self, s):
        def tokenize(s):
            tokens = []
            nums, chs = '', ''
            for ch in s:
                if ch.isdigit():
                    nums += ch
                elif ch in '[]':
                    if chs:
                        tokens.append(chs)
                        chs = ''
                    if nums:
                        tokens.append(nums)
                        nums = ''
                    tokens.append(ch)
                else:
                    chs += ch
            if chs:
                tokens.append(chs)
            return tokens

        def parse(tokens):
            stacks = [[]]
            for token in tokens:
                if token == '[':
                    stacks.append([])
                elif token == ']':
                    sub_stack = stacks.pop()
                    cnt = stacks[-1].pop()
                    stacks[-1].append((cnt, sub_stack))
                else:
                    stacks[-1].append(token)
            return stacks[-1]

        def expand(ast):
            res = []
            for item in ast:
                if isinstance(item, tuple):
                    cnt, stack = item
                    res.append(int(cnt) * expand(stack))
                else:
                    res.append(item)
            return ''.join(res)

        tokens = tokenize(s)
        ast = parse(tokens)
        res = expand(ast)
        return res




class Solution:
    def decodeString(self, s):
        def tokenize(s):
            tokens = []
            nums, chs = '', ''
            for ch in s:
                if ch.isdigit():
                    nums += ch
                elif ch in '[]':
                    if chs:
                        tokens.append(chs)
                        chs = ''
                    if nums:
                        tokens.append(nums)
                        nums = ''
                    tokens.append(ch)
                else:
                    chs += ch
            if chs:
                tokens.append(chs)
            return tokens

        def parse(tokens):
            ast = [[]]
            for token in tokens:
                if token.isdigit():
                    ast[-1].append([token, ''])
                elif token == '[':
                    ast.append([])
                elif token == ']':
                    ast[-1][-1][1] = ast.pop()
                else:
                    ast[-1].append([1, token])
            return ast[-1]

        def gen_s(ast):
            return ''.join(int(cnt) * (val if isinstance(val, str) else gen_s(val)) for cnt, val in ast)

        tokens = tokenize(s)
        ast = parse(tokens)
        res = gen_s(ast)

        return res


class Solution:
    def decodeString(self, s):
        stack = [['', 1]]
        num = ''

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch == ']':
                chs, cnt = stack.pop()
                stack[-1][0] += chs * cnt
            else: # char
                stack[-1][0] += ch

        return stack[0][0]

