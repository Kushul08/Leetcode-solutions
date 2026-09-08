# ─────────────────────────────────────────────────
#  Problem : 3870. Count Commas in Range
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-09-08
# ─────────────────────────────────────────────────

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        return n-999