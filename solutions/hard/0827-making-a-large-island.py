# ─────────────────────────────────────────────────
#  Problem : 0827. Making A Large Island
#  Difficulty : Hard
#  Runtime  : 23 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-07-17
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
        self.components={}
    def find_par(self,node):
        # print(self.parent,node)
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find_par(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        # print('hello')
        ulp_u=self.find_par(u)
        ulp_v=self.find_par(v)
        # print(u,v,ulp_u,ulp_v)
        if ulp_u==ulp_v:
            return
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
            if ulp_v not in self.components:
                self.components[ulp_v]=1
            self.components[ulp_v]+=1
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
            if ulp_u not in self.components:
                self.components[ulp_u]=1
            self.components[ulp_u]+=1
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
            if ulp_u not in self.components:
                self.components[ulp_u]=1
            self.components[ulp_u]+=1
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
                    # print('jejeke',nx,ny)
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        # print('im here')
                        if (nx,ny) not in dsu.parent:
                            dsu.parent[(nx,ny)]=(nx,ny)
                            dsu.rank[(nx,ny)]=0 
                        # print('Calling')  
                        dsu.union((x,y),(nx,ny))
        # print(dsu.components,dsu.parent)
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
                # print(area,components,x,y)
        
        if area==0:
            return n*n
        return area