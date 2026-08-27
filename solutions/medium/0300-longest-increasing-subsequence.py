# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 2822 ms
#  Memory   : 597.9 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        @lru_cache(None)
        def recur(i,prev):
            if i==n:
                return 0
            pick=0
            if prev<nums[i]:
                pick=recur(i+1,nums[i])+1
            unpick=recur(i+1,prev)
            return max(pick,unpick)
        return recur(0,float('-inf'))