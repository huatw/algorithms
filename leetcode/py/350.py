class Solution:
    def intersect(self, nums1, nums2):
        res = []

        m = collections.defaultdict(int)

        for n in nums1:
            m[n] += 1

        for n in nums2:
            if n in m and m[n] > 0:
                m[n] -= 1
                res.append(n)

        return res


class Solution:
    def intersect(self, nums1, nums2):
        res = []

        m = collections.Counter(nums1)

        for n in nums2:
            if n in m and m[n] > 0:
                m[n] -= 1
                res.append(n)

        return res


def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())
