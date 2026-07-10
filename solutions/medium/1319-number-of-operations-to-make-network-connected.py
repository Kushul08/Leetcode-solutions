# ─────────────────────────────────────────────────
#  Problem : 1319. Number of Operations to Make Network Connected
#  Difficulty : Medium
#  Runtime  : 51 ms
#  Memory   : 30.9 MB
#  Solved   : 2026-07-10
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        adj_list=[[] for _ in range(n)]
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        components=0
        visited=[0]*n

        for i in range(n):
            if visited[i]==1:
                continue
            components+=1
            queue=deque()
            queue.append(i)
            while queue:
                node=queue.popleft()
                if visited[node]==1:
                    continue
                visited[node]=1
                for neigh in adj_list[node]:
                    if visited[neigh]==0:
                        queue.append(neigh)
        return components-1