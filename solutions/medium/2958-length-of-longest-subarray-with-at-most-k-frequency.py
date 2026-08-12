# ─────────────────────────────────────────────────
#  Problem : 2958. Length of Longest Subarray With at Most K Frequency
#  Difficulty : Medium
#  Runtime  : 416 ms
#  Memory   : 21.7 MB
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
        l=0
        r=0
        length=0
        while r<len(nums):
            num=nums[r]
            freq[num]=freq.get(num,0)+1
            while freq[num]>k:
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            length=max(length,r-l+1)
            r+=1
        return length