# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        for i in range(3,n+1):
            c=a+b
            a,b=b,c
        return b