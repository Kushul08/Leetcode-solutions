# ─────────────────────────────────────────────────
#  Problem : 0802. Find Eventual Safe States
#  Difficulty : Medium
#  Runtime  : 77 ms
#  Memory   : 17.6 MB
#  Solved   : 2026-06-18
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        queue=deque()
        """
        adj_list=[[] for _ in range(len(graph))]
        queue=deque()
        in_degree=[0]*len(graph)
        safe=[]


        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
            for node in graph[i]:
                adj_list[node].append(i)
            in_degree[i]=len(graph[i])



        while queue:
            root=queue.popleft()
            safe.append(root)
            for node in adj_list[root]:
                in_degree[node]-=1
                if in_degree[node]==0:
                    queue.append(node)
            adj_list[root]=[]
        return sorted(safe)