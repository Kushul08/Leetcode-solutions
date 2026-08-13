# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 27 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if (target+sum(nums))%2!=0 or (target+sum(nums))<0 : return 0
        required=(target+sum(nums))//2
        dp=[0]*(required+1)
        if nums[0]==0:
            dp[0]=2
        else:
            dp[0]=1
            if nums[0]<=required:
                dp[nums[0]]=1
        for i in range(1,n):
            temp=[0]*(required+1)
            for j in range(required+1):
                pick=0
                if nums[i]<=j:
                    pick=dp[j-nums[i]]
                unpick=dp[j]
                temp[j]=pick+unpick
            dp=temp
        return dp[required]
        