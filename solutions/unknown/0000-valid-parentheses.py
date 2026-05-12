# ─────────────────────────────────────────────────
#  Problem : 0000. Valid Parentheses
#  Difficulty : Unknown
#  Runtime  : 3 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-12
# ─────────────────────────────────────────────────

class Solution(object):
    def isValid(self, s):
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char]!=stack.pop():
                   return False
            else:
                return False
        return not stack