# ─────────────────────────────────────────────────
#  Problem : 3499. Maximize Active Section with Trade I
#  Difficulty : Medium
#  Runtime  : 1271 ms
#  Memory   : 14.9 MB
#  Solved   : 2026-07-21
# ─────────────────────────────────────────────────

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        initial=s.count('1')
        zero=[]
        i=0
        while i<n:
            start=i
            while i<n and s[i]==s[start]:
                i+=1
            if s[start]=='0':
                zero.append(i-start)
        m=len(zero)
        if m<2: return initial
        max_=0
        for i in range(m-1):
            max_=max(max_,zero[i]+zero[i+1])
        return initial+max_