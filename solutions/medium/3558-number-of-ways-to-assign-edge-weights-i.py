# ─────────────────────────────────────────────────
#  Problem : 3558. Number of Ways to Assign Edge Weights I
#  Difficulty : Medium
#  Runtime  : 638 ms
#  Memory   : 52.3 MB
#  Solved   : 2026-06-11
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n=len(edges)
        adj_list=[[] for _ in range(n+2)]
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        queue=deque([1])
        depth=[-1]*(n+2)
        depth[1]=0
        max_depth=0
        MOD=int(1e9+7)
        while queue:
            node=queue.popleft()
            curr_depth=depth[node]

            if curr_depth>max_depth: max_depth=curr_depth

            for nodes in adj_list[node]:
                if depth[nodes]==-1:
                    depth[nodes]=curr_depth+1
                    queue.append(nodes)
        return pow(2,max_depth-1,MOD)