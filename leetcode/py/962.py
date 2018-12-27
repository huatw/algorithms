class Solution:
    def maxWidthRamp(self, nums):
        res = 0
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < -stack[-1][0]:
                stack.append((-num, -i))
            else:
                idx = bisect.bisect(stack, (-num, -i))
                res = max(res, i + stack[idx][1])
        return res