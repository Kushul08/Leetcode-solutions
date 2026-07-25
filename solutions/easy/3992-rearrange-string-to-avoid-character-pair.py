# ─────────────────────────────────────────────────
#  Problem : 3992. Rearrange String to Avoid Character Pair
#  Difficulty : Easy
#  Runtime  : 2 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-25
# ─────────────────────────────────────────────────

class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        if x not in s or y not in s:
            return s
        if s.rfind(y)<s.index(x):
            return s
        count=s.count(y)
        rem_s=''
        for ch in s:
            rem_s+=ch if ch!=y else ''
        return y*count+rem_s