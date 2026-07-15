# ─────────────────────────────────────────────────
#  Problem : 3658. GCD of Odd and Even Sums
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-15
# ─────────────────────────────────────────────────

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # even= sum of even numbers upto n is n*(n+1)
        # odd=sum of odd numbers upto n is n*n
        # and there gcd is n
        return n