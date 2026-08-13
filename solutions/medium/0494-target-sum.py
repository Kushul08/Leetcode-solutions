# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 43 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if (target+sum(nums))%2!=0 or (target+sum(nums))<0 : return 0
        required=(target+sum(nums))//2
        dp=[[0]*(required+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=0
        if nums[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
            if nums[0]<=required:
                dp[0][nums[0]]=1
        for i in range(1,n):
            for j in range(required+1):
                pick=0
                if nums[i]<=j:
                    pick=dp[i-1][j-nums[i]]
                unpick=dp[i-1][j]
                dp[i][j]=pick+unpick
        return dp[n-1][required]
        