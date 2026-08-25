# ─────────────────────────────────────────────────
#  Problem : 1092. Shortest Common Supersequence
#  Difficulty : Hard
#  Runtime  : 339 ms
#  Memory   : 44.3 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m=len(str1),len(str2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        x,y=n,m
        ans=[]
        while x>0 and y>0:
            if str1[x-1]==str2[y-1]:
                ans.append(str1[x-1])
                x-=1
                y-=1
            elif dp[x-1][y]>dp[x][y-1]:
                ans.append(str1[x-1])
                x-=1
            else:
                ans.append(str2[y-1])
                y-=1
        while x>0:
            ans.append(str1[x-1])
            x-=1
        while y>0:
            ans.append(str2[y-1])
            y-=1
        return ''.join(ans[::-1])