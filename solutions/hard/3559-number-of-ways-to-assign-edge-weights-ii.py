# ─────────────────────────────────────────────────
#  Problem : 3559. Number of Ways to Assign Edge Weights II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-12
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def find_lca(a,b):
            while depth[a]>depth[b]:
                a=parent[a]

            while depth[b]>depth[a]:
                b=parent[b]
            while a!=b:
                a=parent[a]
                b=parent[b]
            return a
        MOD=int(1e9)+7
        n=len(edges)+2
        adj_list=[[] for _ in range(n)]
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        depth=[-1]*n
        depth[1]=0
        visited=[0]*n
        parent=[0]*n
        queue=deque([(1,0)])
        visited[1]=1
        while queue:
            node,dep=queue.popleft()
            for side in adj_list[node]:
                if visited[side]==0:
                    parent[side]=node
                    visited[side]=1
                    queue.append((side,dep+1))
                    depth[side]=dep+1
        # print(depth,parent)
        ans=[]
        for u,v in queries:
            val=depth[u]+depth[v]-2*depth[find_lca(u,v)]
            if val==0:
                ans.append(0)
                continue
            val=pow(2,val-1,MOD)
            ans.append(val)
        return ans