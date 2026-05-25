# ─────────────────────────────────────────────────
#  Problem : 1871. Jump Game VII
#  Difficulty : Medium
#  Runtime  : 303 ms
#  Memory   : 16.1 MB
#  Solved   : 2026-05-25
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        queue=deque([0])
        farthest=0

        while queue:
            i=queue.popleft()
            start=max(i+minJump,farthest+1)
            end=min(i+maxJump,len(s)-1)

            for j in range(start,end+1):
                if s[j]=='0':
                    if j==len(s)-1:
                        return True
                    queue.append(j)
            farthest=end
        return False