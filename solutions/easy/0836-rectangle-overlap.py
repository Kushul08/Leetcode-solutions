# ─────────────────────────────────────────────────
#  Problem : 0836. Rectangle Overlap
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-14
# ─────────────────────────────────────────────────

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,x2=rec1[0],rec1[2]
        y1,y2=rec1[1],rec1[3]
        nx,ny=rec2[0],rec2[1]

        if x1<nx<x2 or y1<ny<y2:
            return True
        return False