# ─────────────────────────────────────────────────
#  Problem : 0169. Majority Element
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 13.6 MB
#  Solved   : 2026-09-01
# ─────────────────────────────────────────────────

class Solution(object):
    def majorityElement(self, nums):
        # hashtable={}
        # for key in nums:
        #     if key in hashtable:
        #         hashtable[key]+=1
        #     else:
        #         hashtable[key]=1
        # max_key=max(hashtable,key=hashtable.get)
        # return max_key

        count=0
        element=None
        for num in nums:
            if count==0:
                count=1
                element=num
            elif element==num:
                count+=1
            else:
                count-=1
        return element