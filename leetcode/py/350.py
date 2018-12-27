class Solution:
    def intersect(self, nums1, nums2):
        res = []

        ch_cnt_map = collections.Counter(nums1)

        for n in nums2:
            if n in ch_cnt_map and ch_cnt_map[n] > 0:
                ch_cnt_map[n] -= 1
                res.append(n)

        return res


def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())
