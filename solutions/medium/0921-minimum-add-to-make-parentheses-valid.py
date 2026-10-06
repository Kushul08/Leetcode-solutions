# ─────────────────────────────────────────────────
#  Problem : 0921. Minimum Add to Make Parentheses Valid
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-10-06
# ─────────────────────────────────────────────────

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open=0
        close=0
        for ch in s:
            if ch=='(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    close+=1

        return open+close