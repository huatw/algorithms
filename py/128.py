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



