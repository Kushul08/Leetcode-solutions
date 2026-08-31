# ─────────────────────────────────────────────────
#  Problem : 1043. Partition Array for Maximum Sum
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n=len(arr)
        def recur(i):
            if i==n:
                return 0
            maxi=-1e9
            for j in range(i,i+min(k,n-i+1)):
                steps=(max(arr[i:j+1])*(j-i+1))+recur(j+1)
                maxi=max(maxi,steps)
            return maxi
        return recur(0)