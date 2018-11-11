class Solution:
    def dailyTemperatures(self, ts):
        res = [0] * len(ts)
        stack = []

        for i, t in enumerate(ts):
            while stack and ts[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
