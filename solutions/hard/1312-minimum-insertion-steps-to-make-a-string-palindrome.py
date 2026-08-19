# ─────────────────────────────────────────────────
#  Problem : 1312. Minimum Insertion Steps to Make a String Palindrome
#  Difficulty : Hard
#  Runtime  : 1171 ms
#  Memory   : 371.4 MB
#  Solved   : 2026-08-19
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s
        s2=s[::-1]

        n=len(s)

        @lru_cache(None)
        def recur(i,j):
            if i<0 or j<0:
                    return 0
            if s1[i]==s2[j]:
                return recur(i-1,j-1)+1
            else:
                return max(recur(i,j-1),recur(i-1,j))
        return n-recur(n-1,n-1)