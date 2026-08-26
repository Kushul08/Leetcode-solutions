# ─────────────────────────────────────────────────
#  Problem : 0044. Wildcard Matching
#  Difficulty : Hard
#  Runtime  : 1215 ms
#  Memory   : 43.5 MB
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
        dp=[[False]*(m+1) for _ in range(n+1)]
        # def recur(i,j):
        #     if i<0 or j<0:
        #         if i<0 and j<0:
        #             return True
        #         elif i<0 and j>=0:
        #             while j>=0 and p[j]=='*':
        #                 j-=1
        #             if j<0:
        #                 return True
        #         return False
        for i in range(n):
            dp[i][0]=False
        for j in range(1,m+1):
            if p[j-1]=='*':
                dp[0][j]=True
            else:
                break
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                elif p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif s[i-1]!=p[j-1]:
                    dp[i][j]=False
                # else:
                #     dp[i][j]=True
        return dp[n][m]