class Solution:
    def repeatedStringMatch(self, from_str, to_str):
        min_times = math.ceil(len(to_str) / len(from_str))
        if to_str in from_str * min_times:
            return min_times
        if to_str in from_str * (min_times + 1):
            return min_times + 1
        return -1
