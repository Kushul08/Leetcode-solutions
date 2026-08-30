# ─────────────────────────────────────────────────
#  Problem : 0312. Burst Balloons
#  Difficulty : Hard
#  Runtime  : 6419 ms
#  Memory   : 16.5 MB
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
        dp=[[-1]*(n) for _ in range(n)]
        def recur(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for indx in range(i,j+1):
                steps=nums[i-1]*nums[indx]*nums[j+1]+recur(i,indx-1)+recur(indx+1,j)
                maxi=max(maxi,steps)
            dp[i][j]=maxi
            return dp[i][j]
        return recur(1,len(nums)-2)