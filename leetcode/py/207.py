# topo
class Solution:
    def canFinish(self, num_courses, prerequisites):
        first_seconds_map = collections.defaultdict(list)
        second_cnt_map = collections.defaultdict(int)
        for second, first in prerequisites:
            first_seconds_map[first].append(second)
            second_cnt_map[second] += 1

        first_courses = [course for course in range(num_courses) if course not in second_cnt_map]
        learned_total = len(first_courses)

        while first_courses:
            first = first_courses.pop()
            for second in first_seconds_map[first]:
                second_cnt_map[second] -= 1
                if second_cnt_map[second] == 0:
                    learned_total += 1
                    first_courses.append(second)

        return learned_total == num_courses

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
