# ─────────────────────────────────────────────────
#  Problem : 0518. Coin Change II
#  Difficulty : Medium
#  Runtime  : 487 ms
#  Memory   : 39 MB
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
        
        dp=[[-1]*(amount+1) for _ in range(n)]
        def recur(i,money):
            if i==-1:
                if money==0:
                    return 1
                return 0
            if dp[i][money]!=-1:
                return dp[i][money]
            pick=0
            if coins[i]<=money:
                pick=recur(i,money-coins[i])
            unpick=recur(i-1,money)
            dp[i][money]=pick+unpick
            return dp[i][money]
        return recur(n-1,amount)