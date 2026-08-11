# ─────────────────────────────────────────────────
#  Problem : 0322. Coin Change
#  Difficulty : Medium
#  Runtime  : 32 ms
#  Memory   : 28.6 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        steps=[float('inf')]
        def recur(i,target,step):
            if i==-1:
                if target==0:
                    steps[0]=min(steps[0],step)
                return
            if coins[i]<=target:
                pick=recur(i-1,target-coins[i],step+1)
                pick_stay=recur(i,target-coins[i],step+1)
            unpick=recur(i-1,target,step)

        recur(n-1,amount,0)
        if steps[0]!=float('inf'):
            return steps[0]
        return -1