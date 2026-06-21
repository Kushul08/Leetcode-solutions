# ─────────────────────────────────────────────────
#  Problem : 3968. Maximum Manhattan Distance After All Moves
#  Difficulty : Medium
#  Runtime  : 337 ms
#  Memory   : 15.9 MB
#  Solved   : 2026-06-21
# ─────────────────────────────────────────────────

class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        pos=[0,0]
        count=0
        for move in moves:
            if move=='L':
                pos[0]-=1
            elif move=='R':
                pos[0]+=1
            elif move=='U':
                pos[1]+=1
            elif move=='D':
                pos[1]-=1
            else:
                count+=1
        for _ in range(count):
            if pos[0]<0:
                pos[0]-=1
            elif pos[0]>0:
                pos[0]+=1
            elif pos[1]<0:
                pos[1]-=1
            elif pos[1]>0:
                pos[1]+=1
            else:
                pos[0]+=1
        return abs(pos[0])+abs(pos[1])