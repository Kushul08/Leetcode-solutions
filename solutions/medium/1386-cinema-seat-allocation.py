# ─────────────────────────────────────────────────
#  Problem : 1386. Cinema Seat Allocation
#  Difficulty : Medium
#  Runtime  : 83 ms
#  Memory   : 16.5 MB
#  Solved   : 2026-08-19
# ─────────────────────────────────────────────────

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        hashmap={}
        for r,c in reservedSeats:
            if r not in hashmap:
                hashmap[r]=[]
            hashmap[r].append(c)
        ans=0
        for key,arr in hashmap.items():
            seats=[True,True,True]
            for c in arr:
                if c==2 or c==3:
                    seats[0]=False
                elif c==4 or c==5:
                    seats[0]=False
                    seats[1]=False
                elif c==6 or c==7:
                    seats[1]=False
                    seats[2]=False
                elif c==8 or c==9:
                    seats[2]=False
            if sum(seats)==3:
                ans+=2
            elif sum(seats)==2:
                if seats[0]==True and seats[2]==True:
                    ans+=2
                else:
                    ans+=1
            elif sum(seats)==1:
                ans+=1 
        ans+=(n-len(hashmap))*2
        return ans