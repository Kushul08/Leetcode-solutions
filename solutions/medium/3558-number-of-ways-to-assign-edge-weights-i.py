# ─────────────────────────────────────────────────
#  Problem : 3558. Number of Ways to Assign Edge Weights I
#  Difficulty : Medium
#  Runtime  : 1105 ms
#  Memory   : 181.6 MB
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
            if b not in adj_list:
                adj_list[b]=[]
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited=set()
        max_depth=[float('-inf')]
        def dfs(node,depth):
            max_depth[0]=max(max_depth[0],depth)
            if node not in adj_list:
                return
            if node not in visited:
                for nodes in adj_list[node]:
                    if nodes not in visited:
                        visited.add(node)
                        dfs(nodes,depth+1)
                        visited.remove(node)
        dfs(1,0)
        if max_depth[0]==0:
            return 2
        ans=pow(2,max_depth[0]-1,int(1e9)+7)
        return ans