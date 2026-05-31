# ─────────────────────────────────────────────────
#  Problem : 0733. Flood Fill
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-31
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        n,m=len(image),len(image[0])
        queue=deque()
        queue.append((sr,sc))

        seen=set()
        org_color=image[sr][sc]
        image[sr][sc]=color
        while queue:
            x,y=queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if image[nx][ny]==org_color and (nx,ny) not in seen:
                    image[nx][ny]=color
                    queue.append((nx,ny))
                    seen.add((nx,ny))
        return image