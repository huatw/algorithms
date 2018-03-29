class Solution(object):
    def reverseStr(self, s, k):
        ret = ''

        for start in range(0, len(s), 2 * k):
            ret += s[start: start + k][::-1] + s[start + k: start + 2 * k]

        return ret




class Solution(object):
    def reverseStr(self, s, k):
        return ''.join([s[start: start + k][::-1] + s[start + k: start + 2 * k] for start in range(0, len(s), 2 * k)])



