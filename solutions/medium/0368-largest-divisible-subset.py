# ─────────────────────────────────────────────────
#  Problem : 0368. Largest Divisible Subset
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-29
# ─────────────────────────────────────────────────

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        dp=[1]*(n)
        hash=[-1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    if dp[i]<dp[j]+1:
                        dp[i]=max(dp[i],dp[j]+1)
                        hash[i]=j
        max_val=max(dp)
        indx=dp.index(max_val)
        ans=[]
        while indx!=-1:
            ans.append(nums[indx])
            indx=hash[indx]
        return ans