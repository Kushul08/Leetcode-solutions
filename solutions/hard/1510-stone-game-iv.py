# ─────────────────────────────────────────────────
#  Problem : 1510. Stone Game IV
#  Difficulty : Hard
#  Runtime  : 830 ms
#  Memory   : 15.8 MB
#  Solved   : 2026-08-10
# ─────────────────────────────────────────────────

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        powers=set([i*i for i in range(1,350)])
        if n in powers:
            return True
        dp=[0]*(n+1)
        dp[0]=False
        dp[1]=True
        if n<2: return dp[n]

        squares=[1]
        for i in range(2,n+1):
            if i in powers:
                squares.append(i)
            sign=True
            for j in squares:
                sign=sign and dp[i-j]
            dp[i]=True if sign==False else False
            
        return dp[n]