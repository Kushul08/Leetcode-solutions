# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        if n<=2:
            return n
        for i in range(3,n+1):
            c=a+b
            a,b=b,c
        return b