class Solution:
    def canFinish(self, numCourses, prerequisites):
        first_seconds_map = collections.defaultdict(list)
        dep_cnt_map = collections.defaultdict(int)

        for (first, second) in prerequisites:
            first_seconds_map[first].append(second)
            dep_cnt_map[second] += 1
            if first not in dep_cnt_map:
                dep_cnt_map[first] = 0

        level = [course for (course, dep_cnt) in dep_cnt_map.items() if dep_cnt == 0]

        while level:
            first = level.pop()
            for second in first_seconds_map[first]:
                dep_cnt_map[second] -= 1
                if dep_cnt_map[second] == 0:
                    level.append(second)

        return all(cnt == 0 for cnt in dep_cnt_map.values())


# BFS
class Solution:
    def canFinish(self, numCourses, prerequisites):
        next_map = collections.defaultdict(list)
        dep_cnt_map = collections.defaultdict(int)
        total_courses = set()
        for (first, second) in prerequisites:
            total_courses.add(first)
            total_courses.add(second)
            dep_cnt_map[second] += 1
            next_map[first].append(second)

        level = set([first for (first, _) in prerequisites if dep_cnt_map[first] == 0])
        seen = set(level)

        while level:
            next_level = []
            for first in level:
                for second in next_map[first]:
                    if second in seen:
                        return False
                    dep_cnt_map[second] -= 1
                    if dep_cnt_map[second] == 0:
                        seen.add(second)
                        next_level.append(second)
            level = next_level
        return len(seen) == len(total_courses)
