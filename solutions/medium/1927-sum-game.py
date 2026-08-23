# ─────────────────────────────────────────────────
#  Problem : 1927. Sum Game
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
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
        if l==r:
            if d==0:
                return False
            return True
        return 9*abs(r-l)!=abs(d)*2 