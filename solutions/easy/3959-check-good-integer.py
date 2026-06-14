# ─────────────────────────────────────────────────
#  Problem : 3959. Check Good Integer
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-14
# ─────────────────────────────────────────────────

class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digitSum=0
        squareSum=0
        while n:
            val=n%10
            digitSum+=val
            squareSum+=pow(val,2)
            n=n//10
        return squareSum - digitSum >= 50