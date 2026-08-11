# ─────────────────────────────────────────────────
#  Problem : 2410. Maximum Matching of Players With Trainers
#  Difficulty : Medium
#  Runtime  : 107 ms
#  Memory   : 24.1 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i=0
        count=0
        for j in range(len(trainers)):
            if i==len(players): break
            if players[i]<=trainers[j]:
                count+=1
                i+=1
        return count