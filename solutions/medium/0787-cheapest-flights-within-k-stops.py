# ─────────────────────────────────────────────────
#  Problem : 0787. Cheapest Flights Within K Stops
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-06-26
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
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
        queue=[]
        heappush(queue,(0,0,src))

        while queue:
            cost,steps,node=heappop(queue)
            if steps-1>k:
                continue
            if node==dst:
                return cost
            for neigh,weight in adj_list[node]:
                if cost+weight<costs[neigh]:
                    costs[neigh]=cost+weight
                    heappush(queue,(costs[neigh],steps+1,neigh))
        return -1