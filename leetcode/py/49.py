# prime numbers
class Solution:
    def groupAnagrams(self, strs):
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 41, 43, 47, 53, 59, 61, 67, 71, 73,
            79, 83, 89, 97, 101, 103
        ]

        groups = collections.defaultdict(list)

        for s in strs:
            hashed = 1
            for ch in s:
                hashed *= primes[ord(ch) - ord('a')]
            groups[hashed].append(s)

        return list(groups.values())


# not ideal
class Solution:
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)

        for s in strs:
            groups[tuple(sorted(s))].append(s)

        return [*groups.values()]



