# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.5 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        if (target+sum(nums))%2!=0: return 0
        required=(target+sum(nums))/2
        def recur(i,exp):
            if i==-1:
                if exp==0:
                    return 1
                return 0
            pick=0
            if nums[i]<=exp:
                pick=recur(i-1,exp-nums[i])
            unpick=recur(i-1,exp)
            return pick+unpick
            
        return recur(n-1,required)