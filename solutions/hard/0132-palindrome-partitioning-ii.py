# ─────────────────────────────────────────────────
#  Problem : 0132. Palindrome Partitioning II
#  Difficulty : Hard
#  Runtime  : 3054 ms
#  Memory   : 22.4 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        n=len(s)
        @lru_cache(None)
        def recur(i):
            if i==n:
                return -1
            mini=1e9
            for k in range(i,n):
                if (i==0 and s[:k+1]==s[k::-1]) or s[i:k+1]==s[k:i-1:-1] :
                    steps=1+recur(k+1)
                    mini=min(mini,steps)
            return mini
        return recur(0)