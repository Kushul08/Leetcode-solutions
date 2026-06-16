# ─────────────────────────────────────────────────
#  Problem : 3612. Process String with Special Operations I
#  Difficulty : Medium
#  Runtime  : 55 ms
#  Memory   : 22.2 MB
#  Solved   : 2026-06-16
# ─────────────────────────────────────────────────

class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        for char in s:
            if char=='*':
                if ans: ans.pop()
            elif char=='#':
                ans+=ans
            elif char=='%':
                ans=ans[::-1]
            else:
                ans.append(char)
        return ''.join(ans)