# ─────────────────────────────────────────────────
#  Problem : 2472. Maximum Number of Non-overlapping Palindrome Substrings
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-09-15
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n=len(s)

        @lru_cache(None)
        def recur(i,j):
            if i==0:
                string=s[i:j+1]
                if len(string)>=k and string==string[::-1]:
                    return 1
                return 0

            if (j-i+1)>=k:
                string=s[i:j+1]
                if string==string[::-1]:
                    return 1+recur(i-1,i-1)
            unpick=recur(i-1,j-1)
            pick=recur(i-1,j)
            return max(unpick,pick)
            
        return recur(n-1,n-1)