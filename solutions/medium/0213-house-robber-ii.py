# ─────────────────────────────────────────────────
#  Problem : 0213. House Robber II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-28
# ─────────────────────────────────────────────────

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=3:
            return max(nums)
        def house_rob(nums):
            n=len(nums)
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]=nums[1]
            dp[2]=max(dp[1],nums[0]+nums[2])
            for i in range(3,n):
                dp[i]=max(dp[i-2],dp[i-3])+nums[i]
            return max(dp[-1],dp[-2])
        return max(house_rob(nums[:-1]),house_rob(nums[1:]))