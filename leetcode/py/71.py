class Solution:
    def simplifyPath(self, path):
        names = path.split('/')
        stack = []

        for name in names:
            if name == '..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)

        return '/' + '/'.join(stack)
