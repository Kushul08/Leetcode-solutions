# ─────────────────────────────────────────────────
#  Problem : 0778. Swim in Rising Water
#  Difficulty : Hard
#  Runtime  : 44 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-17
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        queue=deque()
        queue.append((0,0))
        visited=[[0]*n for _ in range(n)]
        visited[0][0]=1
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        maxi=grid[0][0]
        while queue:
            x,y=queue.popleft()
            maxi=max(maxi,grid[x][y])
            if x==n-1 and y==n-1:
                return maxi
            
            u,v=None,None
            mini=50000

            for dx,dy in directions:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                    if mini>grid[nx][ny]:
                        u,v=nx,ny
                        mini=grid[nx][ny]
            if u!=None and v!=None:
                queue.append((u,v))
                visited[u][v]=1
        return maxi