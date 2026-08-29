# ─────────────────────────────────────────────────
#  Problem : 0673. Number of Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 957 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-08-29
# ─────────────────────────────────────────────────

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n
        count=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    count[i]=count[j]
                elif nums[j]<nums[i] and dp[j]+1==dp[i]:
                    count[i]+=count[j]
        maxi=max(dp)
        ans=0
        for i in range(n):
            if dp[i]==maxi:
                ans+=count[i] 
        return ans