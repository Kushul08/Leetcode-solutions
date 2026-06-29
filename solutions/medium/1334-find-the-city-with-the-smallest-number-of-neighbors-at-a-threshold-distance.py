# ─────────────────────────────────────────────────
#  Problem : 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
#  Difficulty : Medium
#  Runtime  : 1202 ms
#  Memory   : 12.8 MB
#  Solved   : 2026-06-29
# ─────────────────────────────────────────────────

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist=[[float('inf')]*n for _ in range(n)]
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j:
                        dist[i][j]=0
                        continue
                    if dist[i][k]!=float('inf') and dist[k][j]!=float('inf'):

                        dist[i][j]=min(dist[i][j],
                                    dist[i][k]+dist[k][j])
        city_count=n
        city_no=0
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold :
                    count+=1
            if count<=city_count:
                city_count=count
                city_no=i
        return city_no