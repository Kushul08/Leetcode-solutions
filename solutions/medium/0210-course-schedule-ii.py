# ─────────────────────────────────────────────────
#  Problem : 0210. Course Schedule II
#  Difficulty : Medium
#  Runtime  : 3 ms
#  Memory   : 15.5 MB
#  Solved   : 2026-06-15
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inorder=[0]*numCourses
        adj_list=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)
            inorder[a]+=1
        path=[0]*numCourses
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
            return True
        for node in range(numCourses):
            if visited[node]==0:
                path[node]=1
                if dfs(node)==False:
                    return []
                path[node]=0
                
        queue=deque()
        
        for i in range(len(inorder)):
            if inorder[i]==0:
                queue.append(i)
        ans=[]
        while queue:
            node=queue.popleft()
            ans.append(node)
            for side in adj_list[node]:
                inorder[side]-=1
                if inorder[side]==0:
                    queue.append(side)
        return ans