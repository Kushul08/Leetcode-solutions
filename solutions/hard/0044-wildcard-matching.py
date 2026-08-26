# ─────────────────────────────────────────────────
#  Problem : 0044. Wildcard Matching
#  Difficulty : Hard
#  Runtime  : 394 ms
#  Memory   : 53.3 MB
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
        dp=[[-1]*m for _ in range(n)]
        def recur(i,j):
            if i<0 or j<0:
                if i<0 and j<0:
                    return True
                elif i<0 and j>=0:
                    while j>=0 and p[j]=='*':
                        j-=1
                    if j<0:
                        return True
                return False 
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==p[j]:
                dp[i][j]=recur(i-1,j-1)
                return dp[i][j]
            elif p[j]=='*':
                dp[i][j]=recur(i-1,j-1) or recur(i-1,j) or recur(i,j-1)
                return dp[i][j]
            elif p[j]=='?':
                dp[i][j]=recur(i-1,j-1)
                return dp[i][j] 
            elif s[i]!=p[j]:
                dp[i][j]=False
                return dp[i][j]
            dp[i][j]=True
            return dp[i][j]
        return recur(n-1,m-1)