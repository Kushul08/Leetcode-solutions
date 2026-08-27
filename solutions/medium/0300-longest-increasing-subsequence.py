# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        def recur(i,prev):
            if i==n:
                return 0
            pick=0
            if prev<nums[i]:
                pick=recur(i+1,nums[i])+1
            unpick=recur(i+1,prev)
            return max(pick,unpick)
        return recur(0,float('-inf'))