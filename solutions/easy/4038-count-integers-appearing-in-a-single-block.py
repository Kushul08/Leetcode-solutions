# ─────────────────────────────────────────────────
#  Problem : 4038. Count Integers Appearing in a Single Block
#  Difficulty : Easy
#  Runtime  : 2 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-08-30
# ─────────────────────────────────────────────────

class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num]=[]
            hashmap[num].append(i)
        count=0
        for key,val in hashmap.items():
            if len(val)==1:
                count+=1
            else:
                flag=True
                for j in range(1,len(val)):
                    if val[j]-val[j-1]!=1:
                        flag=False
                        break
                if flag:
                    count+=1
        return count