# thought: remove k / 2 elements each time
# optimize O log(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        k = len(nums1) + len(nums2)
        cut_l, cut_r = 0, len(nums1)
        cut1 = len(nums1) // 2

        while 0 <= cut1 <= len(nums1):
            cut1 = (cut_r - cut_l) // 2 + cut_l
            cut2 = k // 2 - cut1

            l1 = -float('inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = -float('inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == len(nums1) else nums1[cut1]
            r2 = float('inf') if cut2 == len(nums2) else nums2[cut2]

            if l1 > r2:
                cut_r = cut1 - 1
            elif l2 > r1:
                cut_l = cut1 + 1
            else:
                l = max(l1, l2)
                r = min(r1, r2)

                return (l + r) / 2 if k % 2 == 0 else r

        return -1