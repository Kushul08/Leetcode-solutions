# ─────────────────────────────────────────────────
#  Problem : 3536. Maximum Product of Two Digits
#  Difficulty : Easy
#  Runtime  : 1 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-25
# ─────────────────────────────────────────────────

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=sorted(str(n))
        return int(num[-1])*int(num[-2])