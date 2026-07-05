# ─────────────────────────────────────────────────
#  Problem : 1301. Number of Paths with Max Score
#  Difficulty : Hard
#  Runtime  : 250 ms
#  Memory   : 13.1 MB
#  Solved   : 2026-07-05
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n=len(board)
        MOD=int(1e9+7)
        directions=[(1,0),(0,1),(1,1)]
        bestscore=[[float('-inf')]*n for _ in range(n)]
        bestscore[0][0]=0
        ways=[[0]*n for _ in range(n)]
        ways[0][0]=1
        grid=[[ch for ch in board[i]] for i in range(n)]
        
        directions=[[1,0],[0,1],[1,1]]
        for i in range(n):
            for j in range(n):
                
                
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if 0<=nx<n and 0<=ny<n:
                        if grid[nx][ny]=='X':
                            continue
                
                        if grid[nx][ny] in 'ES':
                            value=0
                        else:
                            value=int(grid[nx][ny])
                        if bestscore[i][j]==float('-inf'):
                            continue
                        candidate=value+bestscore[i][j]
                        if candidate>bestscore[nx][ny]:
                            bestscore[nx][ny]=candidate
                            ways[nx][ny]=ways[i][j]
                        elif candidate==bestscore[nx][ny]:
                            ways[nx][ny]+=ways[i][j]
                            ways[nx][ny]%=MOD
        if bestscore[n-1][n-1]==float('-inf'):
            return [0,0]
        return [bestscore[n-1][n-1],ways[n-1][n-1]]