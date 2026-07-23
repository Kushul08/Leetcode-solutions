# ─────────────────────────────────────────────────
#  Problem : 0070. Climbing Stairs
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-23
# ─────────────────────────────────────────────────

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(curr):
            if curr>n:
                return 0
            if curr==n:
                return 1
            return climb(curr+1)+climb(curr+2)
        return climb(0)