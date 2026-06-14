# ─────────────────────────────────────────────────
#  Problem : 0210. Course Schedule II
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 15.4 MB
#  Solved   : 2026-06-14
# ─────────────────────────────────────────────────

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)
        path=[0]*numCourses
        stack=[]
        visited=[0]*numCourses 
        def dfs(node):
            visited[node]=1
            for side in adj_list[node]:
                if path[side]==1:
                    return False
                if visited[side]==0:
                    path[side]=1
                    if dfs(side)==False:
                        return False
                    path[side]=0
            stack.append(node)
            return True
        for node in range(numCourses):
            if visited[node]==0:
                path[node]=1
                if dfs(node)==False:
                    return []
                path[node]=0
        ans=[]
        while stack:
            ans.append(stack.pop())
        return ans