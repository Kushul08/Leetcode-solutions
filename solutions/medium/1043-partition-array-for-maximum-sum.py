# ─────────────────────────────────────────────────
#  Problem : 1043. Partition Array for Maximum Sum
#  Difficulty : Medium
#  Runtime  : 247 ms
#  Memory   : 12.4 MB
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
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            maxi=-1e9
            max_val=-1e9
            for j in range(i,min(i+k,n)):
                max_val=max(max_val,arr[j])
                steps=max_val*(j-i+1)+dp[j+1]
                maxi=max(maxi,steps)
            dp[i]=maxi
        return dp[0]
        