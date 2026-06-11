# ─────────────────────────────────────────────────
#  Problem : 0207. Course Schedule
#  Difficulty : Medium
#  Runtime  : 4 ms
#  Memory   : 15.4 MB
#  Solved   : 2026-06-11
# ─────────────────────────────────────────────────

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)
        def dfs(root):
            if visited[root]==0:
                visited[root]=1
                if not adj_list[root]:
                    return True
                for node in adj_list[root]:
                    if path[node]==1:
                        return False
                    path[node]=1
                    if dfs(node)==False:
                        return False
                    path[node]=0
        path=[0]*numCourses
        visited=[0]*numCourses
        for node in range(numCourses):
            if visited[node]==0:
                path[node]=1
                if dfs(node)==False:
                    return False
                path[node]=0
        return True