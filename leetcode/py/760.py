class Solution:
    def anagramMappings(self, A, B):
        num_idx_map = {num: i for i, num in enumerate(B)}
        return [num_idx_map[num] for num in A]

