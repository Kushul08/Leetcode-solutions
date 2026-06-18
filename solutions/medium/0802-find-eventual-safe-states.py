# ─────────────────────────────────────────────────
#  Problem : 0802. Find Eventual Safe States
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-18
# ─────────────────────────────────────────────────

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        is_safe=[-1]*len(graph)
        visited=[0]*len(graph)
        # print(is_safe)
        def dfs(root):
            if is_safe[root]==1:
                return True
            for node in graph[root]:
                if visited[node]==1:
                    return False
                visited[node]=1
                if dfs(node)==False:
                    return False
                visited[node]=0
            return True
        
        for root in range(len(graph)):
            visited[root]=1
            if dfs(root)==True:
                is_safe[root]=1
            else:
                is_safe[root]=0
            visited[root]=0
            
        return [i for i in range(len(is_safe)) if is_safe[i]==1]