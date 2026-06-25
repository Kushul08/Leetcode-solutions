# ─────────────────────────────────────────────────
#  Problem : 1091. Shortest Path in Binary Matrix
#  Difficulty : Medium
#  Runtime  : 246 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-06-25
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if grid[0][0]==1: return -1
        dis=[[float('inf')]*len(grid) for _ in range(len(grid))]
        dis[0][0]=1
        
        queue=deque()
        queue.append((dis[0][0],0,0))

        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while queue:
            d,x,y=queue.popleft()
            if d>dis[x][y]:
                continue
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    if grid[nx][ny]==0 and dis[x][y]+1<dis[nx][ny]:
                        dis[nx][ny]=dis[x][y]+1
                        queue.append((dis[nx][ny],nx,ny))
        if dis[-1][-1]==float('inf'):
            return -1
        return dis[-1][-1]
            