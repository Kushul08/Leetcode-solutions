# ─────────────────────────────────────────────────
#  Problem : 3020. Find the Maximum Number of Elements in Subset
#  Difficulty : Medium
#  Runtime  : 666 ms
#  Memory   : 26.1 MB
#  Solved   : 2026-06-27
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap=Counter(nums)
        seen=set()
        def check(num):
            count=0
            if num==1:
                return hashmap[num]-1 if hashmap[num]%2==0 else hashmap[num]
            while True:
                seen.add(num)
                if hashmap[num]>=2:
                    count+=2
                elif hashmap[num]==1:
                    count+=1
                    break
                else:
                    count-=1
                    break
                nxt=pow(num,2)
                if nxt not in hashmap:
                    count-=1
                    break
                num=nxt
            return count
                    
        
        ans=0
        for num in nums:
            ans=max(ans,check(num))
        return ans