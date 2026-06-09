# ─────────────────────────────────────────────────
#  Problem : 0785. Is Graph Bipartite?
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-06-09
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        visited=[-1]*n
        color=[-1]*n

        for nd in range(n):
            if visited[nd]==-1:

                queue=deque([nd])

                while queue:
                    node=queue.popleft()
                    visited[node]=1
                    if color[node]==-1:
                        color[node]=0
                    for side in graph[node]:
                        if color[side]!=-1:
                            if color[side]==color[node]:
                                return False
                        else:
                            color[side]=1^color[node]
                            queue.append(side)
        return True