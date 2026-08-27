# ─────────────────────────────────────────────────
#  Problem : 0188. Best Time to Buy and Sell Stock IV
#  Difficulty : Hard
#  Runtime  : 169 ms
#  Memory   : 25.7 MB
#  Solved   : 2026-08-27
# ─────────────────────────────────────────────────

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(k+1)]
                for _ in range(2)]
                for _ in range(n)]
        def recur(i,status,k):
            if i==n or k==0:
                return 0
            if dp[i][status][k]!=-1:
                return dp[i][status][k]
            if status==1:
                skip=recur(i+1,status,k)
                sell=recur(i+1,0,k-1)+prices[i]
                dp[i][status][k]=max(skip,sell)
                return dp[i][status][k]
            else:
                skip=recur(i+1,status,k)
                buy=recur(i+1,1,k)-prices[i]
                dp[i][status][k]=max(skip,buy)
                return dp[i][status][k]
        return recur(0,0,k)