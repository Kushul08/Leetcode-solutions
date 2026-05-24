# ─────────────────────────────────────────────────
#  Problem : 1340. Jump Game V
#  Difficulty : Hard
#  Runtime  : 623 ms
#  Memory   : 22.6 MB
#  Solved   : 2026-05-24
# ─────────────────────────────────────────────────

class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n=len(arr)

        dp=[-1]*n

        def dfs(i):
            if dp[i]!=-1:
                return dp[i]
            ans=1
            for step in range(1,d+1):
                
                left=i-step
                if left<0:
                    break
                if arr[left]>=arr[i]:
                    break
                ans=max(ans,1+dfs(left))

            for step in range(1,d+1):

                right=i+step
                if right>=n:
                    break
                if arr[right]>=arr[i]:
                    break
                ans=max(ans,1+dfs(right))

            dp[i]=ans
            return ans
        
        result=1
        for i in range(len(arr)):
            result=max(result,dfs(i))
        return result