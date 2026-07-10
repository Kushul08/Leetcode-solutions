# ─────────────────────────────────────────────────
#  Problem : 1319. Number of Operations to Make Network Connected
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
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
        adj_list=[[] for _ in range(n)]
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        queue=deque()
        queue.append(0)
        visited=[0]*n
        edges=0
        while queue:
            node=queue.popleft()
            if visited[node]==1:
                continue
            # print(node)
            edges+=1
            visited[node]=1
            for neigh in adj_list[node]:
                if visited[neigh]==0:
                    queue.append(neigh)
        # print(edges,visited)
        disconnect=visited.count(0)
        # print(disconnect,total_edges-edges+1)
        total_edges=len(connections)
        if total_edges-edges+1>=disconnect:
            return total_edges-edges+1
        return -1