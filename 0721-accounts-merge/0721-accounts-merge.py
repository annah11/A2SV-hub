class unifind:
    def __init__(self):
        self.par = {}
    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x]) 
        return self.par[x]
    def union(self,x,y):
        self.par[self.find(x)] = self.find(y)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = unifind()
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            f_email = acc[1]
            for email in acc[1:]:
                if email not in uf.par:
                    uf.par[email] = email
                uf.union(f_email,email)
                email_to_name[email] =name
        merged = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            merged[root].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in merged.items()]