# O(n)
class Solution:
    def canReorderDoubled(self, nums):
        num_cnt_map = collections.Counter(nums)
        if 0 in num_cnt_map:
            cnt = num_cnt_map.pop(0)
            if cnt % 2 != 0:
                return False
        level = [num for num in num_cnt_map.keys() if num / 2 not in num_cnt_map]

        while level:
            num = level.pop()
            cnt = num_cnt_map[num]
            num_cnt_map[num] = 0
            next_num = num * 2
            num_cnt_map[next_num] -= cnt
            if num_cnt_map[next_num] < 0:
                return False
            if num_cnt_map[next_num] > 0:
                level.append(next_num)
            elif num_cnt_map[next_num] == 0 and next_num * 2 in num_cnt_map:
                level.append(next_num * 2)

        return all(cnt == 0 for cnt in num_cnt_map.values())




# NlogN
class Solution:
    def canReorderDoubled(self, A):
        count = collections.Counter(A)

        for x in sorted(A, key = abs):
            if count[x] == 0:
                continue
            if count[2*x] == 0:
                return False
            count[x] -= 1
            count[2*x] -= 1

        return True
