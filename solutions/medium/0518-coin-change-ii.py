# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 371 ms
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
        dp=[]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp.append(1)
            else:
                dp.append(0)
        dp[0]=1
        for i in range(1,n):
            for j in range(coins[i],amount+1):
                pick=0
                if coins[i]<=j:
                    pick=dp[j-coins[i]]
                unpick=dp[j]
                dp[j]=pick+unpick
        return dp[amount]