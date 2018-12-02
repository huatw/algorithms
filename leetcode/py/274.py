# Onlogn
class Solution:
    def hIndex(self, citations):
        citations = sorted(citations, reverse=True)

        for i, citation in enumerate(citations):
            if citation < i + 1:
                break
            if i == len(citations) - 1 or i + 2 > citations[i + 1]:
                return i + 1

        return 0


# O(n)
class Solution:
    def hIndex(self, citations):
        citation_cnt = [0] * (len(citations) + 1)
        for citation in citations:
            citation_cnt[min(citation, len(citations))] += 1

        total = 0
        for i in reversed(range(len(citations) + 1)):
            total += citation_cnt[i]
            if total >= i:
                return i
        return 0




# Onlogn
class Solution:
    def hIndex(self, citations):
        citations = sorted(citations, reverse=True)

        for i in range(len(citations)):
            if citations[i] < i + 1:
                break
            if i == len(citations) - 1 or i + 1 >= citations[i + 1]:
                return i + 1

        return 0




# On
class Solution:
    def hIndex(self, citations):
        c_count = [0] * (len(citations) + 1)
        for citation in citations:
            if citation >= len(citations):
                c_count[-1] += 1
            else:
                c_count[citation] += 1

        for i in reversed(range(len(citations))):
            c_count[i] += c_count[i + 1]
            if c_count[i + 1] >= i + 1:
                return i + 1

        return 0