# ─────────────────────────────────────────────────
#  Problem : 3345. Smallest Divisible Digit Product I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-06
# ─────────────────────────────────────────────────

class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def product(num):
            prod=1
            while num:
                prod*=num%10
                num=num//10
            return prod
        for i in range(n,101):
            prod=product(i)
            if prod%t==0:
                return i