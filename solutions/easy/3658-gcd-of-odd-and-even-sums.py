# ─────────────────────────────────────────────────
#  Problem : 3658. GCD of Odd and Even Sums
#  Difficulty : Easy
#  Runtime  : 34 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-07-15
# ─────────────────────────────────────────────────

from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=0
        odd=0
        for i in range(1,2*n+1):
            if i&1==0:
                even+=i
            else:
                odd+=i
        return math.gcd(odd,even)