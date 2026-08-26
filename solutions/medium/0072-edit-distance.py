# ─────────────────────────────────────────────────
#  Problem : 0072. Edit Distance
#  Difficulty : Medium
#  Runtime  : 39 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        if n==0 and m==0:
            return 0
        elif n==0 and m!=0:
            return m
        elif n!=0 and m==0:
            return n
        if len(word1)<len(word2):
            s=word1
            t=word2
        else:
            s=word2
            t=word1
        
        n,m=len(s),len(t)

        dp=[0]*(n+1) 
        for i in range(n+1):
            dp[i]=i

        dp[0]=0
        for i in range(1,m+1):
            temp=[0]*(n+1)
            temp[0]=i
            for j in range(1,n+1):
                if s[j-1]==t[i-1]:
                    temp[j]=dp[j-1]
                else:
                    temp[j]=min(1+dp[j-1],
                                1+temp[j-1],
                                1+dp[j])
            dp=temp
        return dp[n]
            