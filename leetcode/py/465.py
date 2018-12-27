# n!
class Solution:
    def minTransfers(self, transactions):
        def remove_group(balances):
            dq = collections.deque([([0], balances[0])])
            while dq:
                cur_idx, cur_sum = dq.popleft()
                if cur_sum == 0:
                    cur_idx = set(cur_idx)
                    return [balances[i] for i in range(len(balances)) if i not in cur_idx]
                for i in range(cur_idx[-1] + 1, len(balances)):
                    dq.append((cur_idx + [i], cur_sum + balances[i]))

        balance_map = collections.Counter()
        for f, t, amount in transactions:
            balance_map[f] -= amount
            balance_map[t] += amount

        balances = [balance for balance in balance_map.values() if balance != 0]
        res = len(balances)
        while balances:
            res -= 1
            balances = remove_group(balances)
        return res
