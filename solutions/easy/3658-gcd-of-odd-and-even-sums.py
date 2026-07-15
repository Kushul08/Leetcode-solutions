# ─────────────────────────────────────────────────
#  Problem : 3658. GCD of Odd and Even Sums
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-15
# ─────────────────────────────────────────────────

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # even= sum of even numbers upto n is n*(n+1)
        # odd=sum of odd numbers upto n is n*n
        # and there gcd is n
        return n 