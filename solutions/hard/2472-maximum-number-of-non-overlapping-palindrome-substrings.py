# ─────────────────────────────────────────────────
#  Problem : 2472. Maximum Number of Non-overlapping Palindrome Substrings
#  Difficulty : Hard
#  Runtime  : 570 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-09-15
# ─────────────────────────────────────────────────

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        def recur(i,string):
            if i==-1:
                if len(string)>=k and string==string[::-1]:
                    return 1
                return 0
            if len(string)>=k and string==string[::-1]:
                return 1+recur(i-1,'')
            unpick=recur(i-1,'')
            pick=recur(i-1,string+s[i])
            return max(unpick,pick)
            
        return recur(n-1,'')