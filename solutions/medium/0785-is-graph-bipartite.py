# ─────────────────────────────────────────────────
#  Problem : 0785. Is Graph Bipartite?
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-09
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        queue=deque([0])
        color={}
        seen=set()

        for node in range(len(graph)):
            if node not in color:
                color[node]='g'
            seen.add(node)
            for side in graph[node]:
                if side in color:
                    if color[side]==color[node]:
                        return False
                else:
                    adj_color='f' if color[node]=='g' else 'g'
                    color[side]=adj_color
        return True 