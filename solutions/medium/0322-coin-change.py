# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 862 ms
#  Memory   : 19.9 MB
#  Solved   : 2026-08-12
# ─────────────────────────────────────────────────

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[float('inf')]*(amount+1)

        dp[0]=0
        if coins[0]<=amount:
            for j in range(coins[0],amount+1,coins[0]):
                dp[j]=j//coins[0]
        for i in range(1,n):
            temp=[float('inf')]*(amount+1)
            temp[0]=0
            for j in range(1,amount+1):
                pick=float('inf')
                if coins[i]<=j:
                    pick=temp[j-coins[i]]+1
                unpick=dp[j]
                temp[j]=min(pick,unpick)
            dp=temp
        return dp[amount] if dp[amount]!=float('inf') else -1