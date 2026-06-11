# ─────────────────────────────────────────────────
#  Problem : 3558. Number of Ways to Assign Edge Weights I
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-11
# ─────────────────────────────────────────────────

class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        adj_list={}
        for a,b in edges:
            if a not in adj_list:
                adj_list[a]=[]
            adj_list[a].append(b)
        max_depth=[float('-inf')]
        def dfs(node,depth):
            if node not in adj_list:
                max_depth[0]=max(max_depth[0],depth)
                return
            for nodes in adj_list[node]:
                dfs(nodes,depth+1)
        dfs(1,0)
        ans=pow(2,max_depth[0]-1,int(1e9)+7)
        return ans