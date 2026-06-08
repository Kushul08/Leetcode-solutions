# ─────────────────────────────────────────────────
#  Problem : 2161. Partition Array According to Given Pivot
#  Difficulty : Medium
#  Runtime  : 60 ms
#  Memory   : 29.4 MB
#  Solved   : 2026-06-08
# ─────────────────────────────────────────────────

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lesser=[]
        equal=[]
        greater=[]

        for num in nums:
            if num<pivot:
                lesser.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                greater.append(num)
        return lesser+equal+greater