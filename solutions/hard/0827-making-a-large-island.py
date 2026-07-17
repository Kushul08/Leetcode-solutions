# ─────────────────────────────────────────────────
#  Problem : 0827. Making A Large Island
#  Difficulty : Hard
#  Runtime  : 2567 ms
#  Memory   : 74.5 MB
#  Solved   : 2026-07-17
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
        self.components={}
    def find_par(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find_par(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        ulp_u=self.find_par(u)
        ulp_v=self.find_par(v)
        if ulp_u==ulp_v:
            return
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.components[ulp_v]+=self.components[ulp_u]
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
            self.components[ulp_u]+=self.components[ulp_v]
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
            self.components[ulp_u]+=self.components[ulp_v]
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        dsu=DSU()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        area=0

        for x in range(n):
            for y in range(n):
                if grid[x][y]==0:
                    continue
                
                if (x,y) not in dsu.parent:
                    dsu.parent[(x,y)]=(x,y)
                    dsu.rank[(x,y)]=0
                    dsu.components[(x,y)]=1
                for dx,dy in directions:
                    nx,ny=dx+x,dy+y
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        if (nx,ny) not in dsu.parent:
                            dsu.parent[(nx,ny)]=(nx,ny)
                            dsu.rank[(nx,ny)]=0 
                            dsu.components[(nx,ny)]=1
                        dsu.union((x,y),(nx,ny))
        for x in range(n):
            for y in range(n):
            
                if grid[x][y]==1:
                    continue
                
                sides=set()
                components=0
                for dx,dy in directions:
                    nx,ny=dx+x,dy+y
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        parent=dsu.find_par((nx,ny))
                        if  parent not in sides:
                            sides.add(parent)
                            components+=dsu.components[parent]
                area=max(area,components+1)
        if area==0:
            return n*n
        return area