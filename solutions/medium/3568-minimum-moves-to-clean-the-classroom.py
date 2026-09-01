# ─────────────────────────────────────────────────
#  Problem : 3568. Minimum Moves to Clean the Classroom
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.6 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        n,m=len(classroom),len(classroom[0])
        start=None
        l=0
        l_ids={}

        for i in range(len(classroom)):
            for j in range(len(classroom[i])):
                if classroom[i][j]=='S':
                    start=(i,j)
                elif classroom[i][j]=='L':
                    l_ids[(i,j)]=l
                    l+=1
        x,y=start
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        
        target_mask = (1 << l) - 1

        queue=deque([(x,y,energy,0,0)])

        seen=set()
        seen.add((x,y,energy,0))
        while queue:
            fx,fy,e,masks,moves=queue.popleft()

            if masks==target_mask:
                return moves
            if e==0:
                continue
            for dx,dy in directions:
                nx,ny=fx+dx,fy+dy
                if 0<=nx<n and 0<=ny<m and classroom[nx][ny]!='X':
                    next_mask=masks
                    ener=e-1
                    if classroom[nx][ny]=='L':
                        l_id=l_ids[(nx,ny)]
                        next_mask |= (1 << l_id)
                    elif classroom[nx][ny]=='R':
                        ener=energy
                    state=(nx,ny,ener,next_mask)

                    if state not in seen:
                        seen.add(state)
                        queue.append((nx,ny,ener,next_mask,moves+1))
        return -1
        