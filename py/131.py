class Solution:
    def partition(self, s):
        ret = []

        for i in range(1, len(s) + 1):
            first = s[:i]
            if first == first[::-1]:
                arrs = self.partition(s[i:])
                if not arrs:
                    ret.append([first])
                else:
                    for arr in arrs:
                        ret.append([first] + arr)

        return ret