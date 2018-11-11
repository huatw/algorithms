'''
1112223334 2
1231231234
'''
class Solution:
    def leastInterval(self, tasks, n):
        task_counts = list(collections.Counter(tasks).values())
        n_slots = max(task_counts)
        rest = task_counts.count(n_slots)

        return max(len(tasks), (n_slots - 1) * (n + 1) + rest)


class Solution:
    def leastInterval(self, tasks, n):
        task_cnt_map = collections.Counter(tasks)
        hq = [(-cnt, task) for (task, cnt) in task_cnt_map.items()]
        heapq.heapify(hq)
        slot_n = 0

        while hq:
            slot_n += 1
            slot_len = n + 1
            slot_tasks = []

            while slot_len and hq:
                slot_len -= 1
                slot_tasks.append(heapq.heappop(hq))

            for (neg_cnt, task) in slot_tasks:
                cnt = -neg_cnt
                if cnt > 1:
                    heapq.heappush(hq, (-(cnt - 1), task))

        return (slot_n - 1) * (n + 1) + len(slot_tasks)

