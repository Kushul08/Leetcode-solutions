# ─────────────────────────────────────────────────
#  Problem : 1064. Fixed Point
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 13.2 MB
#  Solved   : 2026-05-22
# ─────────────────────────────────────────────────

class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i,num in enumerate(arr):
            if i==num:
                return i
        return -1