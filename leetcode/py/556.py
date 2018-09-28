class Solution:
    def nextGreaterElement(self, n):
        arr = list(map(int, str(n)))

        idx = len(arr) - 1
        while idx > 0 and arr[idx] <= arr[idx - 1]:
            idx -= 1

        if idx == 0:
            return -1

        idx2 = idx
        while idx2 < len(arr) - 1 and arr[idx2 + 1] > arr[idx - 1]:
            idx2 += 1

        arr[idx - 1], arr[idx2] = arr[idx2], arr[idx - 1]
        arr[idx:] = reversed(arr[idx:])
        ret = int(''.join(map(str, arr)))

        return ret if ret <= ((1 << 31) - 1) else -1