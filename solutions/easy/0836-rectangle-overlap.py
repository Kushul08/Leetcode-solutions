# ─────────────────────────────────────────────────
#  Problem : 0836. Rectangle Overlap
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-09-14
# ─────────────────────────────────────────────────

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2=rec1
        x3,y3,x4,y4=rec2

        if x4<=x1 or x2<=x3 or y3>=y2 or y1>=y4:
            return False
        return True