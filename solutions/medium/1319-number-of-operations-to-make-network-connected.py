# ─────────────────────────────────────────────────
#  Problem : 1319. Number of Operations to Make Network Connected
#  Difficulty : Medium
#  Runtime  : 149 ms
#  Memory   : 25.6 MB
#  Solved   : 2026-07-10
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
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        dsu=DSU(n)
        for u,v in connections:
            dsu.union(u,v)
        connected=set()
        for i in range(n):
            connected.add(dsu.find_par(i))    
        print(connected)
        return len(connected)-1