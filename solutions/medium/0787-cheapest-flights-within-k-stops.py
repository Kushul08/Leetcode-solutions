# ─────────────────────────────────────────────────
#  Problem : 0787. Cheapest Flights Within K Stops
#  Difficulty : Medium
#  Runtime  : 4 ms
#  Memory   : 13.4 MB
#  Solved   : 2026-06-26
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
        steps=[float('inf')]*n
        costs[src]=0
        queue=[]
        heappush(queue,(0,0,src))

        ans=float('inf')
        while queue:
            step,cost,node=heappop(queue)
            if node==dst:
                if step<=k+1:
                    ans=min(ans,cost)
                continue 
            if step>k+1:  continue

            for neigh,weight in adj_list[node]:
                if cost+weight<costs[neigh] and step<=k:
                    costs[neigh]=cost+weight
                    heappush(queue,(step+1,costs[neigh],neigh))
        if ans!=float('inf'):
            return ans
        return -1