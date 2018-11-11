# DFS
# todo

# UF
class UnionFind:
    def __init__(self):
        self.m = {}

    def add(self, email):
        if email not in self.m:
            self.m[email] = email

    def union(self, email1, email2):
        root1, root2 = self.find(email1), self.find(email2)
        if root1 != root2:
            self.m[root2] = root1

    def find(self, email):
        if self.m[email] == email:
            return email
        self.m[email] = self.find(self.m[email])
        return self.m[email]

class Solution:
    def accountsMerge(self, accounts):
        def merge_emails(emails_list):
            uf = UnionFind()
            for emails in emails_list:
                root = None
                for email in emails:
                    if not root:
                        root = email
                    uf.add(email)
                    uf.union(root, email)

            root_emails_map = collections.defaultdict(list)
            for email in uf.m.keys():
                root_emails_map[uf.find(email)].append(email)

            return [*root_emails_map.values()]

        name_emails_list_map = collections.defaultdict(list)

        for [name, *emails] in accounts:
            name_emails_list_map[name].append(emails)

        for (name, emails_list) in name_emails_list_map.items():
            name_emails_list_map[name] = merge_emails(emails_list)

        return [[name, *sorted(emails)] for (name, emails_list) in name_emails_list_map.items() for emails in emails_list]
