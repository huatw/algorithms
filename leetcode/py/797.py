# DFS O(n) O(n)
class Solution:
    def allPathsSourceTarget(self, graph):
        path_map = {}

        def recur(start):
            if start not in path_map:
                if graph[start]:
                    paths = [[start] + path for node in graph[start] for path in recur(node)]
                else:
                    paths = [[start]]
                path_map[start] = paths

            return path_map[start]

        return recur(0)

'''
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]

0--->1
|    |
v    v
2--->3 -> 4

0 1 3 4
0 2 3 4
sub-paths after 3 can be shared by 1 and 2
'''