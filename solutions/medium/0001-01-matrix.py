# ─────────────────────────────────────────────────
#  Problem : 0001. 01 Matrix
#  Difficulty : Medium
#  Runtime  : 330 ms
#  Memory   : 17.7 MB
#  Solved   : 2026-06-01
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j,0))
        seen=set()
        res=mat
        while queue:
            x,y,dis=queue.popleft()
            if (x,y) in seen:
                continue
            if x<0 or x>=len(mat) or y<0 or y>=len(mat[0]):
                continue
            if mat[x][y]==1:
                res[x][y]=dis
            seen.add((x,y))
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                queue.append((x+dx,y+dy,dis+1))
        return res
