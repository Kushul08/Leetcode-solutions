# ─────────────────────────────────────────────────
#  Problem : 2574. Left and Right Sum Differences
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-06-06
# ─────────────────────────────────────────────────

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_sum=0
        right_sum=sum(nums)
        ans=[]
        for num in nums:
            right_sum-=num
            ans.append(abs(left_sum-right_sum))
            left_sum+=num
        return ans