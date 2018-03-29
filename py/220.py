# treeset 红黑树

# bucketsort
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}

        for i, v in enumerate(nums):
            bucketNum, offset = (v // t, 1) if t else (v, 0)

            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - v) <= t:
                    return True

            buckets[bucketNum] = v
            if len(buckets) > k:
                del buckets[nums[i - k] // t if t else nums[i - k]]

        return False