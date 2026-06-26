# ─────────────────────────────────────────────────
#  Problem : 0787. Cheapest Flights Within K Stops
#  Difficulty : Medium
#  Runtime  : 24 ms
#  Memory   : 13.3 MB
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
        queue=deque()
        adj_list=[[] for _ in range(n)]
        for n1,n2,cost in flights:
            adj_list[n1].append((n2,cost))
        
        queue.append((0,src,0))
        dis=[float('inf')]*n
        dis[src]=0
        while queue:
            steps,node,cost=queue.popleft()
            print(steps,node,cost)
            if steps>k+1:
                continue
            for neigh,weight in adj_list[node]:
                if cost+weight<dis[neigh] and steps<=k:
                    dis[neigh]=cost+weight
                    queue.append((steps+1,neigh,dis[neigh]))
        if dis[dst]==float('inf'):
            return -1
        return dis[dst]