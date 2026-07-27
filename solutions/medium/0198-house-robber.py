# ─────────────────────────────────────────────────
#  Problem : 0198. House Robber
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-07-27
# ─────────────────────────────────────────────────

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=nums[1]
        max_val=max(dp[0],dp[1])
        for i in range(2,n):
            dp[i]=max(dp[i-2],dp[max(0,i-3)])+nums[i]
            max_val=max(max_val,dp[i])
        return max_val