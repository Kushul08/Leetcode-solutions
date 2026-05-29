# ─────────────────────────────────────────────────
#  Problem : 3300. Minimum Element After Replacement With Digit Sum
#  Difficulty : Easy
#  Runtime  : 7 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-29
# ─────────────────────────────────────────────────

class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=float('inf')
        for num in nums:
            sums=0
            while num>0:
                sums+=(num%10)
                num=num//10
            ans=min(ans,sums)
        return ans