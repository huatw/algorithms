class Solution:
    def longestConsecutive(self, nums):
        n_dis_map = collections.Counter()
        res = 0
        for num in nums:
            if num not in n_dis_map:
                right_dis, left_dis = n_dis_map[num + 1], n_dis_map[num - 1]
                dis = left_dis + right_dis + 1
                res = max(res, dis)
                n_dis_map[num] = dis
                n_dis_map[num + right_dis] = dis
                n_dis_map[num - left_dis] = dis
        return res



# hash map
class Solution:
    def longestConsecutive(self, nums):
        nmap = collections.defaultdict(int)
        res = 0

        for num in nums:
            if nmap[num] == 0:
                left, right = nmap[num - 1], nmap[num + 1]
                nmap[num] = 1 + left + right
                res = max(res, nmap[num])
                nmap[num - left] = nmap[num]
                nmap[num + right] = nmap[num]

        return res




# set: one direction
class Solution:
    def longestConsecutive(self, nums):
        nset = set(nums)
        res = 0

        for num in nset:
            if num - 1 not in nset:
                right_num = num + 1

                while right_num in nset:
                    right_num += 1

                res = max(res, right_num - num + 1)

        return res