# ─────────────────────────────────────────────────
#  Problem : 2149. Rearrange Array Elements by Sign
#  Difficulty : Medium
#  Runtime  : 47 ms
#  Memory   : 42.3 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=0
        neg=1
        ans=[0]*(len(nums))
        for num in nums:
            if num<0:
                ans[neg]=num
                neg+=2
            else:
                ans[pos]=num
                pos+=2
        return ans