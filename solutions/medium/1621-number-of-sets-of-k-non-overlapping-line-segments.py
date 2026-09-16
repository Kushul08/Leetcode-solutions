# ─────────────────────────────────────────────────
#  Problem : 1621. Number of Sets of K Non-Overlapping Line Segments
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-09-16
# ─────────────────────────────────────────────────

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        

        def recur(num,k):
            if num==1:
                if k==0:
                    return 1
                return 0
            skip=recur(num-1,k)
            take=0
            if k>0:
                take=recur(num-1,k-1)
            return (skip+take)
        return recur(n+k-1,k*2)