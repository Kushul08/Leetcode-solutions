# ─────────────────────────────────────────────────
#  Problem : 2472. Maximum Number of Non-overlapping Palindrome Substrings
#  Difficulty : Hard
#  Runtime  : 3130 ms
#  Memory   : 230.2 MB
#  Solved   : 2026-09-15
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)

        pal=[[True]*n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal[i][j] = s[i] == s[j] and (length == 2 or pal[i + 1][j - 1])

        
        @lru_cache(None)
        def recur(i):
            if i>=n:
                return 0
            
            ans=recur(i+1)

            for j in range(i+k-1,n):
                if pal[i][j]:
                    ans=max(ans,1+recur(j+1))
            return ans

        return recur(0)