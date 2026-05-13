# ─────────────────────────────────────────────────
#  Problem : 1674. Minimum Moves to Make Array Complementary
#  Difficulty : Medium
#  Runtime  : 251 ms
#  Memory   : 25.9 MB
#  Solved   : 2026-05-13
# ─────────────────────────────────────────────────

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n=len(nums)
        diff=[0]*(2*limit+2)
        for i in range(n//2):
            a=min(nums[i],nums[n-i-1])
            b=max(nums[i],nums[n-i-1])
            diff[2]+=2 # we assumed every sum demands 2 moves

            diff[a+1]-=1 # but for range of [a+1,b+limit] we require only 1 move i.e intially it is 2
                        # therfeore we subtract -1 here

            diff[a+b]-=1 # as we know a+b lies in the range of a+1,a+limit we need to c (a+b=c) to be 0 beacuse it requires 0 changes so intially it was +2 we made it to +1 now made it to 0 by doing a -1

            diff[a+b+1]+=1 # we need to place remaing elements as it is so we do what we have done at the start of the index i.e we subtracted there and here we  do the opposite we add it .

            diff[limit+b+1]+=1 #this is last index+1 index of the range[a+1,b+limit] after abd before this index all should have a value of +2 at the starting index i.e a+1 we made a -1 which results in 1 and we need to make it 2 because the range is over so adding +1 now onwards (the beauty of diff array and sweep line) 

        min_ops=n # we setted it to n because at worst case every pair have a moves of 2 therfore one eelement have a max move of 1 therefore n elements have n no of moves in worst case 
        oprs=0
        for i in range(2,2*limit+1):
            oprs+=diff[i]
            if oprs<min_ops:
                min_ops=oprs
        return min_ops