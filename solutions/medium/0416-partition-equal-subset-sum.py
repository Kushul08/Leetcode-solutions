# ─────────────────────────────────────────────────
#  Problem : 0416. Partition Equal Subset Sum
#  Difficulty : Medium
#  Runtime  : 1295 ms
#  Memory   : 34.8 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)&1)==1:
            return False
        n=len(nums)
        k=sum(nums)//2

        dp=[[False]*(k+1) for _ in range(n)]

        for i in range(n):
            dp[i][0]=True       
        if nums[0]<=k:        
            dp[0][nums[0]]=True  
        
        for i in range(1,n):
            for j in range(1,k+1):
                dp[i][j]=dp[i-1][j]
                if nums[i]<=j:
                    dp[i][j]=dp[i][j] or dp[i-1][j-nums[i]]
                if j==k and dp[i][j]==True:
                    return True
        return dp[n-1][k]