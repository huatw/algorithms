# TLE O(nlogn)
class Solution:
    def numSquares(self, num):
        res = [0]

        for n in range(1, num+1):
            res.append(math.inf)
            for i in range(1, math.floor(math.sqrt(n)) + 1):
                res[-1] = min(res[-1], res[n - i ** 2] + 1)

        return res[-1]

# TLE O(nlogn)
class Solution:
    def numSquares(self, num):
        res = [0]
        squares = [i ** 2 for i in range(1, math.floor(math.sqrt(num)) + 1)]

        for n in range(1, num+1):
            res.append(math.inf)
            for i2 in squares[:math.floor(math.sqrt(n))]:
                res[-1] = min(res[-1], res[n - i2] + 1)

        return res[-1]

# memo to cheat
class Solution:
    res = [0]

    def numSquares(self, num):

        if len(self.res) <= num:
            squares = [i ** 2 for i in range(1, math.floor(math.sqrt(num)) + 1)]

            for n in range(len(self.res), num+1):
                self.res.append(math.inf)
                for i2 in squares[:math.floor(math.sqrt(n))]:
                    self.res[-1] = min(self.res[-1], self.res[n - i2] + 1)

        return self.res[num]


# BFS nlogn
class Solution:
    def numSquares(self, n):
        if n < 2:
            return n

        lst = [i ** 2 for i in range(1, math.floor(math.sqrt(n)) + 1)]

        cnt = 0 # bfs level
        toCheck = set([n])

        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp

        return cnt