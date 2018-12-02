# O(n) O(k) generalize
def majorityElement(nums, k):
    ctr = collections.Counter()

    for n in nums:
        ctr[n] += 1
        if len(ctr) == k:
            ctr -= collections.Counter(set(ctr))

    ctr = collections.Counter(n for n in nums if n in ctr)

    return [n for n, cnt in ctr.items() if cnt > len(nums) / k]


# O(n) O(1)
class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []

        cnt1, cnt2, candidate1, candidate2 = 0, 0, None, None

        for n in nums:
            if n == candidate1:
                cnt1 += 1
            elif n == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = n, 1
            elif cnt2 == 0:
                candidate2, cnt2 = n, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) / 3]


# O(nlogn) O(1)
class Solution:
    def majorityElement(self, nums):
        nums = sorted(nums)
        cnt = 0
        cur_n = None
        res = []

        for num in nums:
            if cur_n != num:
                cur_n = num
                cnt = 0
            cnt += 1
            if cnt > len(nums) / 3 and (not res or res[-1] != num):
                res.append(cur_n)

        return res



# O(n) O(n)
class Solution:
    def majorityElement(self, nums):
        n_map = collections.defaultdict(int)

        for n in nums:
            n_map[n] += 1

        return [k for k, v in n_map.items() if v > len(nums) / 3]
