# ─────────────────────────────────────────────────
#  Problem : 0200. Number of Islands
#  Difficulty : Medium
#  Runtime  : 247 ms
#  Memory   : 27.9 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue=deque()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    queue.append((i,j))
        islands=0
        while queue:
            x,y=queue.popleft()
            if grid[x][y]=='0':
                continue
            islands+=1
            grid[x][y]='0'

            temp=deque([(x,y)])

            while temp:
                i,j=temp.popleft()
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                        continue
                    if grid[nx][ny]=='1': 
                        grid[nx][ny]='0'
                        temp.append((nx,ny))
        return islands