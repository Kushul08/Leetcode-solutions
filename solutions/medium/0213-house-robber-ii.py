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
        def house_rob(start,end):
            n=end
            first=nums[start]
            second=nums[start+1]
            third=max(second,nums[start]+nums[start+2])
            for i in range(3,n-start):
                curr=max(second,first)+nums[start+i]
                first,second,third=second,third,curr
            return max(second,third)
        return max(house_rob(0,len(nums)-1),house_rob(1,len(nums)))