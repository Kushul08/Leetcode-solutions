# ─────────────────────────────────────────────────
#  Problem : 0721. Accounts Merge
#  Difficulty : Medium
#  Runtime  : 44 ms
#  Memory   : 16.4 MB
#  Solved   : 2026-07-15
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find_par(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find_par(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        ulp_u=self.find_par(u)
        ulp_v=self.find_par(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n=len(accounts)
        dsu=DSU(n)
        emails={}
        for i in range(len(accounts)):
            person=accounts[i]
            for j in range(1,len(person)):
                if person[j] in emails:
                    dsu.union(i,emails[person[j]])
                else:
                    emails[person[j]]=i
        # print(emails)
        parents={}
        for email,par in emails.items():
            parent=dsu.find_par(par)
            if parent not in parents:
                parents[parent]=[email]
            else:
                parents[parent].append(email)
        # print(parents)
        ans=[]
        for par,email in parents.items():
            temp=[accounts[par][0]]
            temp.extend(sorted(email))
            ans.append(temp)
        return ans