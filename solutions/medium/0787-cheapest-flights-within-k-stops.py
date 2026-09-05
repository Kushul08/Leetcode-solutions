# ─────────────────────────────────────────────────
#  Problem : 0787. Cheapest Flights Within K Stops
#  Difficulty : Medium
#  Runtime  : 3 ms
#  Memory   : 13.4 MB
#  Solved   : 2026-09-05
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adj_list=[[] for _ in range(n)]
        for n1,n2,cost in flights:
            adj_list[n1].append((n2,cost))

        costs=[float('inf')]*n
        costs[src]=0
        queue=deque([(0,src,0)])

        while queue:
            cost,node,steps=queue.popleft()
            if steps>=k+1:
                continue
            for neigh,weight in adj_list[node]:
                if cost+weight<costs[neigh]:
                    costs[neigh]=min(costs[neigh],cost+weight)
                    queue.append((costs[neigh],neigh,steps+1))
        if costs[dst]!=float('inf'):
            return costs[dst]
        return -1