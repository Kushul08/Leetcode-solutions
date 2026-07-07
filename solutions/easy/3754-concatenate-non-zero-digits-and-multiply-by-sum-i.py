# ─────────────────────────────────────────────────
#  Problem : 3754. Concatenate Non-Zero Digits and Multiply by Sum I
#  Difficulty : Easy
#  Runtime  : 9 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-07
# ─────────────────────────────────────────────────

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        non_zeros=sums=0
        for num in str(n):
            if int(num)!=0:
                non_zeros=non_zeros*10+int(num)
                sums+=int(num)
        return sums*non_zeros