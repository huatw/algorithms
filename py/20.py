class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) == 0 or stack[-1] not in pair or pair[stack.pop()] != char:
                return False

        return len(stack) == 0
