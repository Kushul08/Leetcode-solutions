# ─────────────────────────────────────────────────
#  Problem : 0130. Surrounded Regions
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 16.1 MB
#  Solved   : 2026-06-01
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        queue=deque()
        n,m=len(board),len(board[0])
        visited=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if board[i][j]=='O':
                        queue.append((i,j))
                        visited[i][j]=1

        while queue:
            x,y=queue.popleft()
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<nx and nx<n-1  and 0<ny and ny<m-1:
                    if board[nx][ny]=='O' and visited[nx][ny]==0:
                        queue.append((nx,ny))
                        visited[nx][ny]=1
        for i in range(n):
            for j in range(m):
                if i!=0 and i!=n-1 and j!=0 and j!=m-1:
                    if board[i][j]=='O' and visited[i][j]==0:
                        board[i][j]='X'