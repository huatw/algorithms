class Solution:
    def strStr(self, source, target):
        if not target:
            return 0
        for i in range(0, len(source) - len(target) + 1):
            for j in range(i, i + len(target)):
                if source[j] == target[j - i]:
                    if (j - i) == len(target) - 1:
                        return i
                else:
                    break

        return -1

