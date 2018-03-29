class Solution:
    def simplifyPath(self, path):
        names = re.findall(r'[^/]+', path)
        stack = []

        for ch in names:
            if ch == '..':
                if len(stack):
                    stack.pop()
            elif ch != '.':
                stack.append(ch)

        res = '/' + '/'.join(stack)

        return res
