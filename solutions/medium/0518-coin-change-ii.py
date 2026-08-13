# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 665 ms
#  Memory   : 63.1 MB
#  Solved   : 2026-08-13
# ─────────────────────────────────────────────────

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for j in range(coins[0],amount+1,coins[0]):
            dp[0][j]=1
        for i in range(1,n):
            for j in range(1,amount+1):
                pick=0
                if coins[i]<=j:
                    pick=dp[i][j-coins[i]]
                unpick=dp[i-1][j]
                dp[i][j]=pick+unpick
        return dp[n-1][amount]