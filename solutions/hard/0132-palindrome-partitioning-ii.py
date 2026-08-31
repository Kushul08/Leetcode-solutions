# ─────────────────────────────────────────────────
#  Problem : 0132. Palindrome Partitioning II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

class Solution:
    def minCut(self, s: str) -> int:
        
        if s==s[::-1]:
            return 0
        n=len(s)
        def recur(i):
            if i==n:
                return -1
            mini=1e9
            for k in range(i,n):
                print(i,k,s[:k+1],s[k::-1],s[:k+1]==s[k::-1])
                if (i==0 and s[:k+1]==s[k::-1]) or s[i:k+1]==s[k:i-1:-1] :
                    print('hello')
                    steps=1+recur(k+1)
                    mini=min(mini,steps)
            return mini
        return recur(0)