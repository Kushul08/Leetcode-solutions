# ─────────────────────────────────────────────────
#  Problem : 3754. Concatenate Non-Zero Digits and Multiply by Sum I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-07-07
# ─────────────────────────────────────────────────

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        prod=1
        sums=0
        while n>0:
            val=n%10
            if val:
                sums+=val
                x=val*prod+x
                prod*=10
            n=n//10
        return sums*x
                