# ─────────────────────────────────────────────────
#  Problem : 2492. Minimum Score of a Path Between Two Cities
#  Difficulty : Medium
#  Runtime  : 201 ms
#  Memory   : 51.7 MB
#  Solved   : 2026-07-04
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        queue=deque()

        queue.append(1)
        adj_list=[[] for _ in range(n+1)]
        for u,v,w in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)
        # print(adj_list)
        visited=[0]*(n+1)
        while queue:
            node=queue.popleft()
            for neigh in adj_list[node]:
                if visited[neigh]==0:
                    queue.append(neigh)
                    visited[neigh]=1
        
        score=int(1e9)
        for u,v,w in roads:
            if visited[u]==1 or visited[v]==1:
                score=min(score,w)
        return score