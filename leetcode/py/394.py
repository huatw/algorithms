'''
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

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

class Solution:
    def decodeString(self, s):
        stack = []
        cnt = ''
        chs = ''
        bracket_cnt = 0

        for ch in s:
            if bracket_cnt > 0: # recursive parse
                chs += ch
                if ch == '[':
                    bracket_cnt += 1
                elif ch == ']':
                    bracket_cnt -= 1
                    if bracket_cnt == 0:
                        stack.append(int(cnt))
                        stack.append(self.decodeString(chs[:-1]))
                        cnt = ''
                        chs = ''
            elif ch.isdigit(): # digit mode
                if chs:
                    stack.append(1)
                    stack.append(chs)
                    cnt = ''
                    chs = ''
                cnt += ch
            elif ch == '[':
                bracket_cnt += 1
            else:
                chs += ch

        if chs:
            stack.append(1)
            stack.append(chs)

        res = ''
        for i in range(0, len(stack), 2):
            res += stack[i] * stack[i + 1]

        return res


