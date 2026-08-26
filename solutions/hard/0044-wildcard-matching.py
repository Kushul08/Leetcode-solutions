# ─────────────────────────────────────────────────
#  Problem : 0044. Wildcard Matching
#  Difficulty : Hard
#  Runtime  : 398 ms
#  Memory   : 149 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n,m=len(s),len(p)
        if n==0 and m!=0:
            if p.count('*')==m:
                return True
            return False
        if n==0 and m==0:
            return True
        if n!=0 and m==0:
            return False
        
        @lru_cache(None)
        def recur(i,j):
            if i<0 or  j<0:
                if i<0 and j<0:
                    return True
                elif i<0 and j>=0:
                    while j>=0 and p[j]=='*':
                        j-=1
                    if j<0:
                        return True
                return False 
            if s[i]==p[j]:
                return recur(i-1,j-1)
            elif p[j]=='*':
                return recur(i-1,j-1) or recur(i-1,j) or recur(i,j-1)
            elif p[j]=='?':
                return recur(i-1,j-1)
            elif s[i]!=p[j]:
                return False
            return True
        return recur(n-1,m-1)