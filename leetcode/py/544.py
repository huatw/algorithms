class Solution:
    def findContestMatch(self, n):
        team = [str(i) for i in range(1, n + 1)]

        while n > 1:
            n //= 2
            for i in range(n):
                team[i] = '({},{})'.format(team[i], team.pop())

        return team[0]
