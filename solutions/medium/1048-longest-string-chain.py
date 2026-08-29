# ─────────────────────────────────────────────────
#  Problem : 1048. Longest String Chain
#  Difficulty : Medium
#  Runtime  : 951 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-29
# ─────────────────────────────────────────────────

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda item: len(item))
        def check(s1,s2):
            i=0
            for j in range(len(s2)):
                if i==len(s1): return True
                if s1[i]==s2[j]:
                    i+=1
            return i==len(s1)
        dp=[1]*len(words)
        for i in range(1,len(words)):
            for j in range(i):
                if len(words[j])+1==len(words[i]):
                    if dp[j]+1>dp[i] and check(words[j],words[i]):
                        dp[i]=dp[j]+1
        return max(dp)