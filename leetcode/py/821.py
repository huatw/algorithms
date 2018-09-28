class Solution:
    def shortestToChar(self, S, C):
        min_left, min_right = [None] * len(S), [None] * len(S)
        min_idx = -float('inf')
        for i, ch in enumerate(S):
            if ch == C:
                min_idx = i
            min_left[i] = i - min_idx

        min_idx = float('inf')
        for i, ch in reversed(list(enumerate(S))):
            if ch == C:
                min_idx = i
            min_right[i] = min_idx - i

        return [min(left, right) for left, right in zip(min_left, min_right)]
