# ─────────────────────────────────────────────────
#  Problem : 0416. Partition Equal Subset Sum
#  Difficulty : Medium
#  Runtime  : 1046 ms
#  Memory   : 19.1 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)&1)==1:
            return False
        n=len(nums)
        k=sum(nums)//2

        dp=[False]*(k+1)
        dp[0]=True

        if nums[0]<=k:        
            dp[nums[0]]=True  

        for i in range(1,n):
            temp=[False]*(k+1)
            for j in range(1,k+1):
                temp[j]=dp[j]
                if nums[i]<=j:
                    temp[j]=temp[j] or dp[j-nums[i]]
            dp=temp
        return dp[k]