# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 378 ms
#  Memory   : 12.8 MB
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
        
        dp=[0]*(amount+1)
        dp[0]=1
        for j in range(coins[0],amount+1,coins[0]):
            dp[j]=1
        for i in range(1,n):
            for j in range(coins[i],amount+1):
                pick=0
                if coins[i]<=j:
                    pick=dp[j-coins[i]]
                unpick=dp[j]
                dp[j]=pick+unpick
        return dp[amount]