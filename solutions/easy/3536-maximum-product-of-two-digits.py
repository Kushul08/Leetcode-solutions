# ─────────────────────────────────────────────────
#  Problem : 3536. Maximum Product of Two Digits
#  Difficulty : Easy
#  Runtime  : 4 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-07-25
# ─────────────────────────────────────────────────

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[]
        for num in str(n):
            result.append(int(num))
        result.sort()
        return result[-1]*result[-2]