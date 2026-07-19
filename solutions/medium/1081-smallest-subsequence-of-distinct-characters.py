# ─────────────────────────────────────────────────
#  Problem : 1081. Smallest Subsequence of Distinct Characters
#  Difficulty : Medium
#  Runtime  : 3 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-19
# ─────────────────────────────────────────────────

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            while stack and stack[-1]>s[i] and stack[-1] in s[i+1:] and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
        return ''.join(stack) 