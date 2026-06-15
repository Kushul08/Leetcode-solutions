# ─────────────────────────────────────────────────
#  Problem : 0207. Course Schedule
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 13.2 MB
#  Solved   : 2026-06-15
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree=[0]*numCourses
        adj_list=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[b].append(a)
            in_degree[a]+=1
        
        queue=deque()

        for i in range(len(in_degree)):
            if in_degree[i]==0:
                queue.append(i)
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for neigh in adj_list[node]:
                in_degree[neigh]-=1
                if in_degree[neigh]==0:
                    queue.append(neigh)
        if count==numCourses:
            return True
        return False