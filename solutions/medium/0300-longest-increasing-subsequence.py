# ─────────────────────────────────────────────────
#  Problem : 0300. Longest Increasing Subsequence
#  Difficulty : Medium
#  Runtime  : 7 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-29
# ─────────────────────────────────────────────────

from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        for num in nums:
            if not temp or temp[-1]<num:
                temp.append(num)
            else:
                indx=bisect_left(temp,num)
                temp[indx]=num
        return len(temp)