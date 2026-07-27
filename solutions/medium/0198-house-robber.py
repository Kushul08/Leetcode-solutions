# ─────────────────────────────────────────────────
#  Problem : 0198. House Robber
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-07-27
# ─────────────────────────────────────────────────

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        def recur(i):
            if i>=n:
                return 0

            pick=nums[i]+recur(i+2)
            unpick=recur(i+1)
            return max(pick,unpick)
        return recur(0)