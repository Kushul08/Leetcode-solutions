# ─────────────────────────────────────────────────
#  Problem : 0921. Minimum Add to Make Parentheses Valid
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-10-06
# ─────────────────────────────────────────────────

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for ch in s:
            if ch=='(':
                stack.append(ch)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)