# ─────────────────────────────────────────────────
#  Problem : 3286. Find a Safe Walk Through a Grid
#  Difficulty : Medium
#  Runtime  : 99 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-02
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        n,m=len(grid),len(grid[0])
        # Again smells me like a Dijkstra
        queue=[]
        if grid[0][0]==1: health-=1
        if health<=0: return False
        heappush(queue,(-health,0,0))
        directions=[(0,-1),(1,0),(0,1),(-1,0)]

        best=[[-1]*m for _ in range(n)]
        best[0][0]=health

        while queue:
            heal,x,y=heappop(queue)
            heal=heal*-1
            if x==n-1 and y==m-1:
                if heal>=1: return True
                else: return False
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m:
                    rem_health=heal-grid[nx][ny]
                    if rem_health>0 and rem_health>best[nx][ny]:
                        best[nx][ny]=rem_health
                        # rem_health=rem_health*-1
                        heappush(queue,(-1*rem_health,nx,ny))

        return False