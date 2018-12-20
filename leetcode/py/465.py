class Solution:
    def minTransfers(self, transactions):
        def remove_group(balances):
            N = len(balances)
            dq = collections.deque([([0], balances[0])])
            while dq:
                cur_set, cur_sum = dq.popleft()
                if cur_sum == 0:
                    cur_set = set(cur_set)
                    return [balances[i] for i in range(N) if i not in cur_set]
                for i in range(cur_set[-1] + 1, N):
                    dq.append((cur_set + [i], cur_sum + balances[i]))

        balance_map = collections.Counter()
        for f, t, amount in transactions:
            balance_map[f] -= amount
            balance_map[t] += amount

        balances = [balance for balance in balance_map.values() if balance != 0]
        total = len(balances)
        while len(balances) > 0:
            balances = remove_group(balances)
            total -= 1
        return total