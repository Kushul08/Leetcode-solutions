# ─────────────────────────────────────────────────
#  Problem : 2574. Left and Right Sum Differences
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-06-06
# ─────────────────────────────────────────────────

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        right_sum=[0]*n
        sums=0
        for i in range(len(nums)-1,-1,-1):
            right_sum[i]=sums
            sums+=nums[i]
        left_sum=0
        ans=[]
        for i in range(n):
            ans.append(abs(left_sum-right_sum[i]))
            left_sum+=nums[i]
        return ans