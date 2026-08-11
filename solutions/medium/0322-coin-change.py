# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 1893 ms
#  Memory   : 133.7 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def recur(i,target):
            if i==-1:
                if target==0:
                    return 0
                return float('inf')
            if dp[i][target]!=-1:
                return dp[i][target]
            pick=float('inf')
            pick_stay=float('inf')
            if coins[i]<=target:
                pick=recur(i-1,target-coins[i])+1
                pick_stay=recur(i,target-coins[i])+1
            unpick=recur(i-1,target)

            dp[i][target]=min(pick,unpick,pick_stay)
            return dp[i][target]

        coin_change=recur(n-1,amount)
        if coin_change!=float('inf'):
            return coin_change
        return -1