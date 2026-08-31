# ─────────────────────────────────────────────────
#  Problem : 0132. Palindrome Partitioning II
#  Difficulty : Hard
#  Runtime  : 3 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        s=' '+s+' '
        def recur(i,j):
            if i==j:
                return 0
            if (i==0 and s[i:j+1]==s[j::-1]) or s[i:j+1]==s[j:i-1:-1] :
                return 0
            mini=1e9
            for k in range(i,j+1):
                steps=1+recur(i,k-1)+recur(k+1,j)
                mini=min(mini,steps)
            return mini
        return recur(1,len(s)-1)