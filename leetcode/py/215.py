# this question is important
'''
          0                # 1  => 2*(2^0 - 1) = 0
    1            2         # 2  => 2*(2^1 - 1) = 2
 3     4      5     6      # 4  => 2*(2^2 - 1) = 6
7 8  9  10  11 12 13 14    # 8  => 2*(2^3 - 1) = 14
f(h) = 1 + 2 + 4 + .. 2^h = 2 * (2 ^ n - 1)
'''
def heapify(lst):
    """Transform list into a heap, in-place, in O(len(lst)) time."""
    n = len(lst)
    for i in reversed(range(n//2)):
        _siftup(lst, i)

def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


# priority q
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]


class Solution:
    def findKthLargest(self, nums, k):
        hq = []
        for num in nums:
            if len(hq) == k:
                heapq.heappushpop(hq, num)
            else:
                heapq.heappush(hq, num)

        return hq[0]



# quick selection O(n)?
class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return 0

        left, right = 0, len(nums)-1

        while True:
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else:
                left = pos + 1


    def partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right

        while l <= r:
            if (nums[l] < pivot and nums[r] > pivot):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1

        nums[left], nums[r] = nums[r], nums[left]
        return r


