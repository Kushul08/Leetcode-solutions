# ─────────────────────────────────────────────────
#  Problem : 1927. Sum Game
#  Difficulty : Medium
#  Runtime  : 201 ms
#  Memory   : 16.5 MB
#  Solved   : 2026-08-23
# ─────────────────────────────────────────────────

class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        half=len(num)//2
        l=r=0
        d=0
        for i in range(len(num)):
            if num[i]=='?':
                if i<half:
                    l+=1
                else:
                    r+=1
            else:
                if i<half:
                    d+=int(num[i])
                else:
                    d-=int(num[i])
        return (l+r)%2==1 or d!=(r-l)*9//2