# ─────────────────────────────────────────────────
#  Problem : 1020. Number of Enclaves
#  Difficulty : Medium
#  Runtime  : 135 ms
#  Memory   : 19.9 MB
#  Solved   : 2026-06-01
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m=len(grid),len(grid[0])
        queue=deque()
        visited=set()
        total_ones=0
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        queue.append((i,j))
                        visited.add((i,j))
                else:
                    total_ones+=1 if grid[i][j]==1 else 0
                    
        changes=0
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            x,y=queue.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<nx and nx<n-1 and 0<ny and ny<m-1:
                    if grid[nx][ny]==1 and (nx,ny) not in visited:
                        changes+=1
                        queue.append((nx,ny))
                        visited.add((nx,ny))
        return total_ones-changes
