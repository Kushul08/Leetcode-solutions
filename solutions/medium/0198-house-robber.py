# ─────────────────────────────────────────────────
#  Problem : 0198. House Robber
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-07-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)

        @lru_cache
        def recur(i):
            if i>=n:
                return 0

            pick=nums[i]+recur(i+2)
            unpick=recur(i+1)
            return max(pick,unpick)
        return recur(0)