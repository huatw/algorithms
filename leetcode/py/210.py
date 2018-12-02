class Solution:
    def findOrder(self, num_courses, prerequisites):
        first_seconds_map = collections.defaultdict(list)
        second_cnt_map = collections.defaultdict(int)
        for second, first in prerequisites:
            first_seconds_map[first].append(second)
            second_cnt_map[second] += 1

        first_courses = [course for course in range(num_courses) if course not in second_cnt_map]
        learned_total = len(first_courses)
        res = []

        while first_courses:
            first = first_courses.pop()
            res.append(first)
            for second in first_seconds_map[first]:
                second_cnt_map[second] -= 1
                if second_cnt_map[second] == 0:
                    learned_total += 1
                    first_courses.append(second)

        return res if learned_total == num_courses else []



class Solution:
    def findOrder(self, numCourses, prerequisites):
        next_map = collections.defaultdict(list)
        dep_cnt_map = collections.defaultdict(int)
        total_courses = set()
        for (second, first) in prerequisites:
            total_courses.add(first)
            total_courses.add(second)
            dep_cnt_map[second] += 1
            next_map[first].append(second)

        level = set([first for (_, first) in prerequisites if dep_cnt_map[first] == 0])
        seen = set(level)
        res = list(level)

        while level:
            next_level = []
            for first in level:
                for second in next_map[first]:
                    if second in seen:
                        return []
                    dep_cnt_map[second] -= 1
                    if dep_cnt_map[second] == 0:
                        res.append(second)
                        seen.add(second)
                        next_level.append(second)
            level = next_level

        if len(seen) == len(total_courses):
            return res + [i for i in range(numCourses) if i not in seen]
        return []
