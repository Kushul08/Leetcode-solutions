# ─────────────────────────────────────────────────
#  Problem : 3471. Find the Largest Almost Missing Integer
#  Difficulty : Easy
#  Runtime  : 15 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-18
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if n==k: return max(nums)
        hashmap=Counter(nums)
        if k==1:
            ans=float('-inf')
            for key,val in hashmap.items():
                if val==1 and key>ans:
                    ans=key
            if ans==float('-inf'): return -1
            return ans
                
        elif k<n:
            if hashmap[nums[0]]==1 and hashmap[nums[-1]]==1:
                return max(nums[0],nums[-1])
            elif hashmap[nums[0]]==1:
                return nums[0]
            elif hashmap[nums[-1]]==1:
                return nums[-1]
        return -1