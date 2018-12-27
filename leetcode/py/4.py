class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        L = len(nums1) + len(nums2)
        lo, hi = 0, len(nums1)
        cut1 = len(nums1) // 2
        while 0 <= cut1 <= len(nums1):
            cut1 = (hi - lo) // 2 + lo
            cut2 = L // 2 - cut1

            l1 = -float('inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = -float('inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == len(nums1) else nums1[cut1]
            r2 = float('inf') if cut2 == len(nums2) else nums2[cut2]

            if l1 > r2:
                hi = cut1 - 1
            elif l2 > r1:
                lo = cut1 + 1
            else:
                l, r = max(l1, l2), min(r1, r2)
                return (l + r) / 2 if L % 2 == 0 else r

        return -1
