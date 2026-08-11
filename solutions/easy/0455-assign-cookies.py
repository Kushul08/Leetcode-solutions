# ─────────────────────────────────────────────────
#  Problem : 0455. Assign Cookies
#  Difficulty : Easy
#  Runtime  : 28 ms
#  Memory   : 13.9 MB
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
        for j in range(len(s)):
            if i==len(g): break
            if g[i]<=s[j]:
                count+=1
                i+=1
        return count