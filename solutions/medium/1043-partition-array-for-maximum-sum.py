# ─────────────────────────────────────────────────
#  Problem : 1043. Partition Array for Maximum Sum
#  Difficulty : Medium
#  Runtime  : 2275 ms
#  Memory   : 16.4 MB
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
        dp=[-1]*(n)
        def recur(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            maxi=-1e9
            max_val=-1e9
            for j in range(i,min(i+k,n)):
                max_val=max(max_val,arr[j])
                steps=(max(arr[i:j+1])*(j-i+1))+recur(j+1)
                maxi=max(maxi,steps)
            dp[i]=maxi
            return dp[i]
        return recur(0)