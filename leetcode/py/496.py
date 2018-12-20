class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n_biggest_map = {}
        biggest = []
        for num in nums2[::-1]:
            while biggest and biggest[-1] <= num:
                biggest.pop()
            n_biggest_map[num] = biggest[-1] if biggest else -1
            biggest.append(num)

        return [n_biggest_map[num] for num in nums1]
