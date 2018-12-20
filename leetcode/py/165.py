class Solution:
    def compareVersion(self, version1, version2):
        v1, v2 = [int(n) for n in version1.split('.')], [int(n) for n in version2.split('.')]
        for n1, n2 in itertools.zip_longest(v1, v2):
            if n2 == None:
                if n1 > 0:
                    return 1
            elif n1 == None:
                if n2 > 0:
                    return -1
            elif n1 > n2:
                return 1
            elif n2 > n1:
                return -1
        return 0




class Solution:
    def compareVersion(self, version1, version2):
        v1, v2 = [int(n) for n in version1.split('.')], [int(n) for n in version2.split('.')]

        for i, (n1, n2) in enumerate(zip(v1, v2)):
            if n1 > n2:
                return 1
            if n2 > n1:
                return -1

        if any(n > 0 for n in v1[i + 1:]):
            return 1
        if any(n > 0 for n in v2[i + 1:]):
            return -1

        return 0