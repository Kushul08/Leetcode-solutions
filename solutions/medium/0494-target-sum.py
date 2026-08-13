# ─────────────────────────────────────────────────
#  Problem : 0494. Target Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
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
        ans=[0]
        def recur(i,exp):
            if i==-1:
                if exp==target:
                    ans[0]+=1
                return
            recur(i-1,exp+nums[i])
            recur(i-1,exp-nums[i])
        recur(n-1,0)
        return ans[0]