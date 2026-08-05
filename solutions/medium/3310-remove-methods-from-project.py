# ─────────────────────────────────────────────────
#  Problem : 3310. Remove Methods From Project
#  Difficulty : Medium
#  Runtime  : 1173 ms
#  Memory   : 197.2 MB
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
        for node in suspicious:
            for par in parent[node]:
                if par not in suspicious:
                    return [i for i in range(n)]

        return [i for i in range(n) if i not in suspicious]