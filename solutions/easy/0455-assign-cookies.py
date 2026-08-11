# ─────────────────────────────────────────────────
#  Problem : 0455. Assign Cookies
#  Difficulty : Easy
#  Runtime  : 31 ms
#  Memory   : 14.1 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i=j=0
        count=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count