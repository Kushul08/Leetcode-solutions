# ─────────────────────────────────────────────────
#  Problem : 0312. Burst Balloons
#  Difficulty : Hard
#  Runtime  : 4039 ms
#  Memory   : 14.4 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,1)
        nums.append(1)
        n=len(nums)
        dp=[[0]*(n) for _ in range(n)]
        for i in range(len(nums)-2,0,-1):
            for j in range(i,len(nums)-1):
                maxi=float('-inf')
                for indx in range(i,j+1):
                    steps=nums[i-1]*nums[indx]*nums[j+1]+dp[i][indx-1]+dp[indx+1][j]
                    maxi=max(maxi,steps)
                dp[i][j]=maxi
        return dp[1][n-2]