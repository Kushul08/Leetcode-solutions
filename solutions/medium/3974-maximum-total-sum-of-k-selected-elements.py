# ─────────────────────────────────────────────────
#  Problem : 3974. Maximum Total Sum of K Selected Elements
#  Difficulty : Medium
#  Runtime  : 312 ms
#  Memory   : 21.2 MB
#  Solved   : 2026-06-28
# ─────────────────────────────────────────────────

class Solution(object):
    def maxSum(self, nums, k, mul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        ans=0
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if k==0:
                break
            if mul>0:
                ans+=nums[i]*mul
                mul-=1
            else:
                ans+=nums[i]
            k-=1
        return ans