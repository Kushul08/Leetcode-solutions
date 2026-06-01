# ─────────────────────────────────────────────────
#  Problem : 1765. Map of Highest Peak
#  Difficulty : Medium
#  Runtime  : 1182 ms
#  Memory   : 121.2 MB
#  Solved   : 2026-06-01
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=isWater
        n,m=len(isWater),len(isWater[0])
        visited=[[0 for _ in range(m)] for _ in range(n)]
        queue=deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]==1:
                    queue.append((i,j,0))
                    ans[i][j]=0
                    visited[i][j]=1
        while queue:
            x,y,dis=queue.popleft()
            visited[x][y]=1
            if isWater[x][y]==0:
                ans[x][y]=dis
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx and nx<n and 0<=ny and ny<m:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        queue.append((nx,ny,dis+1))
        return ans