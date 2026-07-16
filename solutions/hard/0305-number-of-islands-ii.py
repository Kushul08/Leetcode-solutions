# ─────────────────────────────────────────────────
#  Problem : 0305. Number of Islands II
#  Difficulty : Hard
#  Runtime  : 257 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-07-16
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self,m,n):
        self.rank={}
        self.parent={}
        for i in range(m):
            for j in range(n):
                self.parent[(i,j)]=(i,j)
                self.rank[(i,j)]=0
    def find_par(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find_par(self.parent[node])
        return self.parent[node]
    def union(self,n1,n2):
        ulp_u=self.find_par(n1)
        ulp_v=self.find_par(n2)
        if ulp_u==ulp_v:
            return
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_u]=ulp_v
            self.rank[ulp_v]+=1
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        dsu=DSU(m,n)
        count=0
        ans=[]
        grid=[[0]*n for _ in range(m)]
        for x,y in positions:
            if grid[x][y]==1:
                ans.append(count)
                continue
            count+=1
            grid[x][y]=1
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny]==1 and dsu.find_par((x,y))!=dsu.find_par((nx,ny)):
                        count-=1
                        dsu.union((nx,ny),(x,y))
            ans.append(count)
        return ans