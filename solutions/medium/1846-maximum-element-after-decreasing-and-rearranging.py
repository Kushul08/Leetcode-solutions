# ─────────────────────────────────────────────────
#  Problem : 1846. Maximum Element After Decreasing and Rearranging
#  Difficulty : Medium
#  Runtime  : 54 ms
#  Memory   : 20.6 MB
#  Solved   : 2026-06-28
# ─────────────────────────────────────────────────

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        if arr[0]!=1:
            arr[0]=1
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])>1:
                arr[i]=arr[i-1]+1
        return max(arr)