'''
Input:
[
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
'''
class Solution:
    def numUniqueEmails(self, emails):
        def normalize(local):
            real_local, _ = local.split('+', 1)
            return ''.join(real_local.split('.'))

        domain_local_map = collections.defaultdict(list)

        for email in emails:
            local, domain = email.split('@')
            domain_local_map[domain].append(local)

        res = 0
        for _, locals in domain_local_map.items():
            seen = set()
            for local in locals:
                nomalized_local = normalize(local)
                if nomalized_local not in seen:
                    seen.add(nomalized_local)
                    res += 1

        return res