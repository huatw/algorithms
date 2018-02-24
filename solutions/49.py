class Solution:
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)

        for s in strs:
            groups[tuple(sorted(s))].append(s)

        return [*groups.values()]



