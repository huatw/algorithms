class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        ch_pair = None
        cnt = 0

        for a, b in zip(A, B):
            if a != b:
                if cnt > 2:
                    return False
                cnt += 1
                if not ch_pair:
                    ch_pair = (a, b)
                else:
                    if (b, a) != ch_pair:
                        return False

        return cnt == 2 or (cnt == 0 and any(cnt >= 2 for cnt in collections.Counter(A).values()))