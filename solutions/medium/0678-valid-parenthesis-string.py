# ─────────────────────────────────────────────────
#  Problem : 0678. Valid Parenthesis String
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-24
# ─────────────────────────────────────────────────

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        asterisks=[]
        opens=[]
        for i,char in enumerate(s):
            if char=='(':
                opens.append(i)
            elif char=='*':
                asterisks.append(i)
            else:
                if opens:
                    opens.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
        while asterisks and opens:
            if opens.pop()>asterisks.pop():
                return False
        if opens:
            return False
        return True