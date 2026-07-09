# ─────────────────────────────────────────────────
#  Problem : 3532. Path Existence Queries in a Graph I
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-09
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
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        dsu=DSU(n)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]-nums[i]<=maxDiff:
                    dsu.union(i,j)
                else:
                    break
        ans=[]
        for u,v in queries:
            if dsu.find_par(u)==dsu.find_par(v):
                ans.append(True)
            else:
                ans.append(False)
        return ans