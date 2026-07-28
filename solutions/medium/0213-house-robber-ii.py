# ─────────────────────────────────────────────────
#  Problem : 0213. House Robber II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-07-28
# ─────────────────────────────────────────────────

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=3:
            return max(nums)
        def house_rob(nums):
            n=len(nums)
            dp=[0]*n
            first=nums[0]
            second=nums[1]
            third=max(second,nums[0]+nums[2])
            for i in range(3,n):
                curr=max(second,first)+nums[i]
                first,second,third=second,third,curr
            return max(second,third)
        return max(house_rob(nums[:-1]),house_rob(nums[1:]))