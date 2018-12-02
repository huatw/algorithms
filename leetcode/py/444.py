class Solution:
    def sequenceReconstruction(self, org, seqs):
        first_seconds_map = collections.defaultdict(list)
        second_cnt_map = collections.defaultdict(int)
        nodes = set(node for seq in seqs for node in seq)

        for seq in seqs:
            for (prev_node, next_node) in zip(seq, seq[1:]):
                first_seconds_map[prev_node].append(next_node)
                second_cnt_map[next_node] += 1

        frees = [node for node in nodes if second_cnt_map[node] == 0]
        res = []
        while len(frees) == 1:
            first = frees.pop()
            res.append(first)
            for second in first_seconds_map[first]:
                second_cnt_map[second] -= 1
                if second_cnt_map[second] == 0:
                    frees.append(second)

        return len(frees) == 0 and len(res) == len(nodes) and res == org