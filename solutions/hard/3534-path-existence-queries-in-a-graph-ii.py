# ─────────────────────────────────────────────────
#  Problem : 3534. Path Existence Queries in a Graph II
#  Difficulty : Hard
#  Runtime  : 2966 ms
#  Memory   : 77 MB
#  Solved   : 2026-07-10
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        ulp_u=self.find(u)
        ulp_v=self.find(v)
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
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        LOG=18
        order = sorted((nums[i], i) for i in range(n))
        values = [x for x, _ in order]
        original = [idx for _, idx in order]

        pos = [0] * n
        for i in range(n):
            pos[original[i]] = i

        dsu = DSU(n)

        for i in range(n - 1):
            if values[i + 1] - values[i] <= maxDiff:
                dsu.union(original[i], original[i + 1])

        farthest = [0] * n

        r = 0
        for l in range(n):

            while r < n and values[r] - values[l] <= maxDiff:
                r += 1

            farthest[l] = r - 1

        up = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = farthest[i]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]
        ans=[]
        for u, v in queries:

            if dsu.find(u) != dsu.find(v):
                ans.append(-1)
                continue

            if u == v:
                ans.append(0)
                continue

            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            cur = left
            jumps = 0
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    jumps += (1 << k)

            ans.append(jumps + 1)

        return ans