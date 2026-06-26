# ─────────────────────────────────────────────────
#  Problem : 1976. Number of Ways to Arrive at Destination
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-26
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD=int(1e9+7)
        adj_list=[[] for _ in range(n)]
        for u,v,w in roads:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        dis=[int(1e9+7)]*n
        ways=[int(1e9+7)]*n
        dis[0]=0
        ways[0]=1
        queue=[]
        heappush(queue,(0,0))
        count=0
        while queue:
            cost,node=heappop(queue)
            if cost>dis[node]:
                continue
            for v,w in adj_list[node]:
                if cost+w==dis[v]:
                    ways[v]+=ways[node]
                if cost+w<dis[v]:
                    ways[v]=ways[node]
                    dis[v]=cost+w
                    heappush(queue,(dis[v],v))
        return ways[-1]%MOD