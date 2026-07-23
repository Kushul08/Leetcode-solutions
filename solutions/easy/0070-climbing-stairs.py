# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def climb(n):
            if n<0:
                return 0
            if n==0:
                return 1
            return climb(n-1)+climb(n-2)
        return climb(n)