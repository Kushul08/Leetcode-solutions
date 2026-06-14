# ─────────────────────────────────────────────────
#  Problem : 0210. Course Schedule II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
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