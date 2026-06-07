# ─────────────────────────────────────────────────
#  Problem : 0200. Number of Islands
#  Difficulty : Medium
#  Runtime  : 273 ms
#  Memory   : 31.3 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen=set()
        queue=deque()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    queue.append((i,j))
        islands=0
        while queue:
            x,y=queue.popleft()
            if (x,y) in seen:
                continue
            islands+=1
            seen.add((x,y))

            temp=deque([(x,y)])

            while temp:
                i,j=temp.popleft()
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                        continue
                    if grid[nx][ny]=='1' and (nx,ny) not in seen:
                        seen.add((nx,ny))
                        temp.append((nx,ny))
        return islands