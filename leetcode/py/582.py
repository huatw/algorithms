class Solution:
    def killProcess(self, pids, ppids, kill):
        pid_ppid_map = collections.defaultdict(list)

        for (pid, ppid) in zip(pids, ppids):
            pid_ppid_map[ppid].append(pid)

        res = []
        stack = [kill]
        while stack:
            id = stack.pop()
            res.append(id)
            stack.extend(pid_ppid_map[id])

        return res