# ─────────────────────────────────────────────────
#  Problem : 3982. Sum of Integers with Maximum Digit Range
#  Difficulty : Easy
#  Runtime  : 52 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-07-05
# ─────────────────────────────────────────────────

class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        max_val=0
        for num in nums:
            string=str(num)
            mini=float('inf')
            maxi=float('-inf')
            for ch in string:
                mini=min(mini,int(ch))
                maxi=max(maxi,int(ch))
            diff=maxi-mini
            max_val=max(max_val,diff)
            if diff in hashmap:
                hashmap[diff].append(num)
            else:
                hashmap[diff]=[num]
        ans=0
        for num in hashmap[max_val]:
            ans+=num
        return ans