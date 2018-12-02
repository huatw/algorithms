# O(n) time and O(1) memory
class Solution:
    def firstWillWin(self, n):
        cache = {0: False, 1: True, 2: True}

        def recur(n):
            if n not in cache:
                cache[n] = not recur(n - 1) or not recur(n - 2)
            return cache[n]

        recur(n)
        return cache[n]




# O(n) time and O(1) memory
class Solution:
    def firstWillWin(self, n):
        return n % 3 != 0
