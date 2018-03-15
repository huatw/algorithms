# sliding window
class Solution:
    def checkInclusion(self, s1, s2):
        t, m = len(s1), collections.Counter(s1)
        start = 0
        for end, ch in enumerate(s2):
            if ch in m:
                while m[ch] == 0:
                    m[s2[start]] += 1
                    t += 1
                    start += 1

                m[ch] -= 1
                t -= 1
                if t == 0:
                    return True
            else:
                while start < end:
                    m[s2[start]] += 1
                    t += 1
                    start += 1
                start += 1

        return False



# sliding window
class Solution:
    def checkInclusion(self, s1, s2):
        total, str_m = len(s1), collections.Counter(s1)

        start, t, m = 0, total, str_m.copy()

        for end, ch in enumerate(s2):
            if ch in m:
                while m[ch] == 0:
                    m[s2[start]] += 1
                    t += 1
                    start += 1

                m[ch] -= 1
                t -= 1
                if t == 0:
                    return True
            else:
                start, t, m = end + 1, total, str_m.copy()

        return False




class Solution(object):
    def checkInclusion(self, s1, s2):
        c1, c2 = collections.Counter(s1), collections.Counter(s2[:len(s1) - 1])

        for i in range(len(s2) - len(s1) + 1):
            c2[s2[i + len(s1) - 1]] += 1

            if len(c1 - c2) == 0:
                return True

            c2[s2[i]] -= 1

        return False


