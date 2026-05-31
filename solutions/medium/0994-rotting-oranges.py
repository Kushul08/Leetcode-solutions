# ─────────────────────────────────────────────────
#  Problem : 0994. Rotting Oranges
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-31
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m=len(grid),len(grid[0])
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j))
        
        seen=set()
        minutes=0
        while queue:
            temp=queue
            queue=deque()
            while temp:
                x,y=temp.popleft()
                for dx,dy in [[-1,0],[0,1],[0,-1],[1,0]]:
                    nx,ny=x+dx,y+dy
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                    if grid[nx][ny]==1 and (nx,ny) not in seen:
                        queue.append((nx,ny))
                        seen.add((nx,ny))
                        grid[nx][ny]=2
            minutes+=1


        for row in grid:
            if 1 in row: return -1
        return minutes-1 if minutes!=0 else minutes