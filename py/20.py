class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            elif pairs[ch] != stack.pop():
                return False

        return len(stack) == 0
