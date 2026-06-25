# ─────────────────────────────────────────────────
#  Problem : 3739. Count Subarrays With Majority Element II
#  Difficulty : Hard
#  Runtime  : 9649 ms
#  Memory   : 21.6 MB
#  Solved   : 2026-06-25
# ─────────────────────────────────────────────────

from sortedcontainers import SortedList
from bisect import bisect_left,bisect_right
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr=[-1 if num!=target else 1 for num in nums]
        prefix=[0]
        for num in arr:
            prefix.append(num+prefix[-1])
        sorted_prefix=SortedList()
        count=0
        for num in prefix:
            subarrays=bisect_left(sorted_prefix,num)
            count+=subarrays
            sorted_prefix.add(num)
        return count