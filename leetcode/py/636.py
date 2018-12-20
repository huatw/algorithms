class Solution:
    def exclusiveTime(self, n, logs):
        stack = []
        res = [0] * n
        prev_ts = 0

        for log in logs:
            id, action, ts = log.split(':')
            if action == 'start':
                if stack:
                    res[stack[-1]] += int(ts) - prev_ts
                stack.append(int(id))
                prev_ts = int(ts)
            else:
                res[stack.pop()] += int(ts) - prev_ts + 1
                prev_ts = int(ts) + 1

        return res
