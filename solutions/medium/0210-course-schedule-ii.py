# ─────────────────────────────────────────────────
#  Problem : 0210. Course Schedule II
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 15.5 MB
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
        visited=[0]*numCourses 
        path=[0]*numCourses 
        def acyclic(root):
            if visited[root]==0:
                visited[root]=1
                for node in adj_list[root]:
                    if path[node]==1:
                        return False
                    path[node]=1
                    if acyclic(node)==False:
                        return False
                    path[node]=0
            return True
        for node in range(numCourses):
            if visited[node]==0:
                path[node]=1
                if acyclic(node)==False:
                    return []
                path[node]=0
        stack=[]
        visited=[0]*numCourses 
        def dfs(node):
            visited[node]=1
            for side in adj_list[node]:
                if visited[side]==0:
                    dfs(side)
            stack.append(node)
            
        for node in range(numCourses):
            if visited[node]==0:
                dfs(node)
        ans=[]
        while stack:
            ans.append(stack.pop())
        return ans