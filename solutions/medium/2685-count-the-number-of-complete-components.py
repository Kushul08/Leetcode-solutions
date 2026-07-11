# ─────────────────────────────────────────────────
#  Problem : 2685. Count the Number of Complete Components
#  Difficulty : Medium
#  Runtime  : 143 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-11
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find_parent(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find_parent(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        ulp_u=self.find_parent(u)
        ulp_v=self.find_parent(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_u]=ulp_v
            self.rank[ulp_v]+=1
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj_list=[[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        dsu=DSU(n)
        for u,v in edges:
            dsu.union(u,v)
        components={}
        for i in range(n):
            parent=dsu.find_parent(i)
            if  parent in components:
                components[parent].append(i)
            else:
                components[parent]=[i]
        count=0
        for key,val in components.items():
            max_conn=len(val)-1
            flag=True
            for node in val:
                if len(adj_list[node])!=max_conn:
                    flag=False
            if flag:
                count+=1
        return count