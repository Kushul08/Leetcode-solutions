# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 55 ms
#  Memory   : 23.4 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if (target+sum(nums))%2!=0 or (target+sum(nums))<0 : return 0
        required=(target+sum(nums))//2
        # if required<0: required+=sum(nums)
        dp=[[-1]*(required+1) for _ in range(n)]
        def recur(i,exp):
            if i==-1:
                if exp==0:
                    return 1
                return 0
            if dp[i][exp]!=-1:
                return dp[i][exp]
            pick=0
            if nums[i]<=exp:
                pick=recur(i-1,exp-nums[i])
            unpick=recur(i-1,exp)
            dp[i][exp]=pick+unpick
            return dp[i][exp]
        return recur(n-1,required)