class Solution:
    def findCircleNum(self, M):
        circle_map = collections.defaultdict(list)

        for i, row in enumerate(M):
            for j, relation in enumerate(row):
                if relation == 1:
                    circle_map[i].append(j)

        res = 0
        seen_set = set()

        for k, arr in circle_map.items():
            if k not in seen_set:
                seen_set.add(k)
                res += 1
                stack = arr
                for friend in stack:
                    if friend not in seen_set:
                        seen_set.add(friend)
                        stack += circle_map[friend]

        return res

