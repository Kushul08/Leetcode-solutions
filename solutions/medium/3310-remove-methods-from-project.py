# ─────────────────────────────────────────────────
#  Problem : 3310. Remove Methods From Project
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-08-05
# ─────────────────────────────────────────────────

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        parent=[[] for _ in range(n)]
        adj_list=[[] for _ in range(n)]

        for u,v in invocations:
            adj_list[u].append(v)
            parent[v].append(u)
        
        suspicious=set()
        
        def dfs(node):
            if node in suspicious:
                return 
            suspicious.add(node)
            for neigh in adj_list[node]:
                dfs(neigh)                
        dfs(k)
        ans=[i for i in range(n)]
        for node in suspicious:
            for par in parent[node]:
                if par not in suspicious:
                    return ans

        for node in suspicious:
            ans.remove(node)
        return ans