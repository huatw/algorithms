class Solution(object):
    def reverseWords(self, s):
        return ' '.join([word for word in reversed(s.split())])
