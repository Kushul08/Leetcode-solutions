# ─────────────────────────────────────────────────
#  Problem : 3559. Number of Ways to Assign Edge Weights II
#  Difficulty : Hard
#  Runtime  : 2452 ms
#  Memory   : 96.6 MB
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
        n=len(edges)+2
        
        LOG=n.bit_length()
        def find_lca(a,b):
            if depth[a]<depth[b]:
                a,b=b,a
            a=lift(a,depth[a]-depth[b])
            if a==b:
                return a
            for j in range(LOG-1,-1,-1):
                if up[a][j]!=up[b][j]:
                    a=up[a][j]
                    b=up[b][j]
            return parent[a]
        MOD=int(1e9)+7
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
        up=[[0]*LOG for _ in range(n)]
        for node in range(1,n):
            up[node][0]=parent[node]
        for j in range(1,LOG):
            for node in range(1,n):
                up[node][j]=up[up[node][j-1]][j-1]
        def lift(node,k):
            for j in range(LOG):
                if k&(1<<j):
                    node=up[node][j]
            return node
        
        ans=[]
        for u,v in queries:
            val=depth[u]+depth[v]-2*depth[find_lca(u,v)]
            if val==0:
                ans.append(0)
                continue
            val=pow(2,val-1,MOD)
            ans.append(val)
        return ans