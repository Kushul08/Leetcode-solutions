# ─────────────────────────────────────────────────
#  Problem : 0525. Contiguous Array
#  Difficulty : Medium
#  Runtime  : 113 ms
#  Memory   : 15.8 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        l=r=0
        max_len=0
        hashmap={0:-1}
        while r<n:
            if nums[r]==0:
                ans+=-1
            else:
                ans+=1
            if ans in hashmap:
                max_len=max(max_len,r-hashmap[ans])
            else:
                hashmap[ans]=r
            r+=1
        return max_len