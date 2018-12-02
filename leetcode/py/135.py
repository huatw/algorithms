class Solution:
    def candy(self, ratings):
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        res = [1] * len(ratings)

        for i, rating in enumerate(ratings):
            if i == 0:
                pass
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
                pass
            else:
                if ratings[i - 1] >= rating > ratings[i + 1]:
                    res[i] = res[i + 1] + 1
                elif rating > ratings[i - 1] and rating > ratings[i + 1]:
                    res[i] = max(res[i - 1], res[i + 1]) + 1
        return sum(res)
