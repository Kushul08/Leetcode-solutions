# ─────────────────────────────────────────────────
#  Problem : 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
#  Difficulty : Medium
#  Runtime  : 292 ms
#  Memory   : 13.4 MB
#  Solved   : 2026-06-29
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adj_list=[[] for _ in range(n)]
        for u,v,w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        count_cities=n
        city_no=0
        for src in range(n):
            queue=[]
            dist=[float('inf')]*n
            dist[src]=0
            heappush(queue,(0,src))
            
            while queue:
                step,node=heappop(queue)
                for v,w in adj_list[node]:
                    if step+w<dist[v]:
                        dist[v]=step+w
                        heappush(queue,(dist[v],v))
            dist[src]=1e9
            count=0
            for d in dist:
                if d<=distanceThreshold: count+=1
            if count<=count_cities:
                count_cities=count
                city_no=src
        return city_no 