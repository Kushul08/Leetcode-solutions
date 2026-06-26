# ─────────────────────────────────────────────────
#  Problem : 1631. Path With Minimum Effort
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-26
# ─────────────────────────────────────────────────

from heapq import heappop, heappush
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n,m=len(heights),len(heights[0])
        max_abs=[[1e9]*m for _ in range(n)]

        max_abs[0][0]=0
        queue=[]
        heappush(queue,(0,0,0))
        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        while queue:
            diff,x,y=heappop(queue)
            if diff>max_abs[x][y]:
                continue
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m:
                    curr_abs=abs(heights[x][y]-heights[nx][ny])
                    max_so_far=max(max_abs[x][y],curr_abs)
                    if max_so_far<max_abs[nx][ny]:
                        max_abs[nx][ny]=max_so_far
                        heappush(queue,(max_so_far,nx,ny))
        return max_abs[-1][-1]