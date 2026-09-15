# ─────────────────────────────────────────────────
#  Problem : 2472. Maximum Number of Non-overlapping Palindrome Substrings
#  Difficulty : Hard
#  Runtime  : 348 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-15
# ─────────────────────────────────────────────────

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def check(i,j):
            length=(j-i+1)
            if length<k:
                return False
            string=s[i:j+1]
            return string==string[::-1]

        ans=0
        i=0
        j=1
        n=len(s)

        while i<n:
            j=i+1
            while j<n:
                if check(i,j):
                    ans+=1
                    i=j
                    break
                j+=1
            i+=1
        return ans