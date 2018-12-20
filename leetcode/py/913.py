class Solution:
    def catMouseGame(self, graph):
        N = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        def get_prev(m, c, turn):
            if turn == CAT:
                for m2 in graph[m]:
                    yield m2, c, MOUSE
            else:
                for c2 in graph[c]:
                    if c2 != 0:
                        yield m, c2, CAT

        state_map = collections.defaultdict(int)
        dependency = {}
        for m in range(N):
            for c in range(N):
                dependency[(m, c, MOUSE)] = len(graph[m])
                dependency[(m, c, CAT)] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        dq = collections.deque()
        for pos in range(N):
            for turn in range(1, 3):
                state_map[(0, pos, turn)] = MOUSE
                dq.append((0, pos, turn, MOUSE))
                if pos > 0:
                    state_map[(pos, pos, turn)] = CAT
                    dq.append((pos, pos, turn, CAT))

        while dq:
            m, c, turn, winner = dq.popleft()
            for prev_m, prev_c, prev_turn in get_prev(m, c, turn):
                if state_map[(prev_m, prev_c, prev_turn)] == DRAW:
                    if prev_turn == winner or dependency[(prev_m, prev_c, prev_turn)] == 1:
                        state_map[(prev_m, prev_c, prev_turn)] = winner
                        dq.append((prev_m, prev_c, prev_turn, winner))
                    else:
                        dependency[(prev_m, prev_c, prev_turn)] -= 1

        return state_map[(1, 2, MOUSE)]
