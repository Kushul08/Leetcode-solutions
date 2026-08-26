# ─────────────────────────────────────────────────
#  Problem : 0044. Wildcard Matching
#  Difficulty : Hard
#  Runtime  : 1218 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n,m=len(s),len(p)
        if n==0 and m!=0:
            if p.count('*')==m:
                return True
            return False
        if n==0 and m==0:
            return True
        if n!=0 and m==0:
            return False
        dp=[False]*(m+1) 
        for j in range(1,m+1):
            if p[j-1]=='*':
                dp[j]=True
            else:
                break
        dp[0]=True
        for i in range(1,n+1):
            temp=[False]*(m+1)
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    temp[j]=dp[j-1]
                elif p[j-1]=='*':
                    temp[j]=dp[j] or temp[j-1]
                else:
                    temp[j]=False
            dp=temp
        return dp[m]