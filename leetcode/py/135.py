class Solution:
    def candy(self, ratings):
        if not ratings:
            return 0

        N = len(ratings)
        left, right = [1] * N, [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in reversed(range(N - 1)):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        return sum(max(l, r) for l, r in zip(left, right))



class Solution:
    def candy(self, ratings):
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        res = [1] * len(ratings)

        for i, rating in enumerate(ratings):
            if i == 0:
                continue
            elif i == len(ratings) - 1:
                if rating > ratings[i - 1]:
                    res[i] = res[i - 1] + 1
            else:
                if ratings[i - 1] < rating <= ratings[i + 1]:
                    res[i] = res[i - 1] + 1
        for i, rating in reversed(list(enumerate(ratings))):
            if i == 0:
                if rating > ratings[i + 1]:
                    res[i] = res[i + 1] + 1
            elif i == len(ratings) - 1:
                continue
            else:
                if ratings[i - 1] >= rating > ratings[i + 1]:
                    res[i] = res[i + 1] + 1
                elif rating > ratings[i - 1] and rating > ratings[i + 1]:
                    res[i] = max(res[i - 1], res[i + 1]) + 1
        return sum(res)
