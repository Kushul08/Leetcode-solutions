# ─────────────────────────────────────────────────
#  Problem : 0210. Course Schedule II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 13.1 MB
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
        if len(ans)==numCourses:
            return ans
        return []