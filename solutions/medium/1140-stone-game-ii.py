# ─────────────────────────────────────────────────
#  Problem : 1140. Stone Game II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-09
# ─────────────────────────────────────────────────

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n=len(piles)
        alice=[0]
        def recur(i,a,b,m,turn):
            if i==n:
                return a
            
            
            if turn:
                ans=float('-inf')

                for x in range(i,min(i+2*m-1,n-1)+1):
                    stones=sum(piles[i:x+1])
                    taken=x-i+1
                    ans=max(ans,recur(x+1,a+stones,b,max(m,taken),False))
                return ans
            else:
                ans=float('inf')

                for x in range(i,min(i+2*m-1,n-1)+1):
                    stones=sum(piles[i:x+1])
                    taken=x-i+1
                    ans=min(ans,recur(x+1,a,b+stones,max(m,taken),True))
                return ans
        return recur(0,0,0,1,True)