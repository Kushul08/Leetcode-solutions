# ─────────────────────────────────────────────────
#  Problem : 1358. Number of Substrings Containing All Three Characters
#  Difficulty : Medium
#  Runtime  : 91 ms
#  Memory   : 13.9 MB
#  Solved   : 2026-06-30
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=b=c=-1
        ans=0
        for i in range(len(s)):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            ans+=min(a,b,c)+1
        return ans
