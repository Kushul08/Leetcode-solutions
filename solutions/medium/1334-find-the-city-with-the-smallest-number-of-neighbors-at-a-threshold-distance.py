# ─────────────────────────────────────────────────
#  Problem : 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
#  Difficulty : Medium
#  Runtime  : 479 ms
#  Memory   : 13 MB
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
        neigh_cities=[0]*n
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j:
                        dist[i][j]=0
                        continue
                    dist[i][j]=min(dist[i][j],
                                    dist[i][k]+dist[k][j])
        for i in range(n):
            for j in range(n):
                if dist[i][j]<=distanceThreshold :
                    neigh_cities[i]+=1
        min_cities=min(neigh_cities)
        for i in range(len(neigh_cities)-1,-1,-1):
            if neigh_cities[i]==min_cities:
                return i
        