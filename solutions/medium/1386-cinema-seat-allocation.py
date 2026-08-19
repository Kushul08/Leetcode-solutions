# ─────────────────────────────────────────────────
#  Problem : 1386. Cinema Seat Allocation
#  Difficulty : Medium
#  Runtime  : 110 ms
#  Memory   : 15.1 MB
#  Solved   : 2026-08-19
# ─────────────────────────────────────────────────

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reservedSeats.sort()
        row=reservedSeats[0][0]
        ans=0
        row_count=0
        seats=[True,True,True]
        for r,c in reservedSeats:
            if row!=r:
                row=r
                row_count+=1
                if sum(seats)==3:
                    ans+=2
                elif sum(seats)==2:
                    if seats[0]==True and seats[2]==True:
                        ans+=2
                    else:
                        ans+=1
                elif sum(seats)==1:
                    ans+=1 
                seats=[True,True,True]
            if row==r:
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
        row_count+=1
        ans+=(n-row_count)*2
        return ans

