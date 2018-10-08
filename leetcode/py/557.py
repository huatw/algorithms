class Solution:
    def reverseWords(self, s):
        words = list(map(lambda s: s[::-1], s.split()))
        return ' '.join(words)

