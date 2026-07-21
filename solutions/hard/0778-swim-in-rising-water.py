# ─────────────────────────────────────────────────
#  Problem : 0778. Swim in Rising Water
#  Difficulty : Hard
#  Runtime  : 32 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-21
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        visited=[[0]*n for _ in range(n)]
        visited[0][0]=1
        queue=[]

        heappush(queue,(grid[0][0],0,0))
        directions=[[-1,0],[1,0],[0,1],[0,-1]]

        while queue:
            max_val,x,y=heappop(queue)
            if x==n-1 and y==n-1:
                return max_val
            for dx,dy in directions:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    heappush(queue,(max(max_val,grid[nx][ny]),nx,ny))
