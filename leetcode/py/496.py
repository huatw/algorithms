class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n_map = {}
        stack = []

        for n in nums2:
            n_map[n] = -1

            while stack and stack[-1] < n:
                n_map[stack.pop()] = n

            stack.append(n)

        return [n_map[n] for n in nums1]
