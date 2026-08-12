# ─────────────────────────────────────────────────
#  Problem : 2958. Length of Longest Subarray With at Most K Frequency
#  Difficulty : Medium
#  Runtime  : 350 ms
#  Memory   : 21.6 MB
#  Solved   : 2026-08-12
# ─────────────────────────────────────────────────

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        l,length=0,0
        for r,num in enumerate(nums):
            freq[num]=freq.get(num,0)+1
            while freq[num]>k:
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            length=max(length,r-l+1)
        return length