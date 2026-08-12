# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 988 ms
#  Memory   : 23.2 MB
#  Solved   : 2026-08-12
# ─────────────────────────────────────────────────

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[float('inf')]*(amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0]=0
        if coins[0]<=amount:
            for j in range(coins[0],amount+1,coins[0]):
                dp[0][j]=j//coins[0]
        
        for i in range(1,n):
            for j in range(1,amount+1):
                pick=float('inf')
                if coins[i]<=j:
                    pick=dp[i][j-coins[i]]+1
                unpick=dp[i-1][j]
                dp[i][j]=min(pick,unpick)
        return dp[n-1][amount] if dp[n-1][amount]!=float('inf') else -1