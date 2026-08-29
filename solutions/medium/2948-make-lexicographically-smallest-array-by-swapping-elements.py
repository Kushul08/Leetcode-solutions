# ─────────────────────────────────────────────────
#  Problem : 2948. Make Lexicographically Smallest Array by Swapping Elements
#  Difficulty : Medium
#  Runtime  : 342 ms
#  Memory   : 84.2 MB
#  Solved   : 2026-08-29
# ─────────────────────────────────────────────────

class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        numssorted=sorted(nums)
        currgroup=0
        num_group={}
        group_list={}
        num_group[numssorted[0]]=currgroup

        group_list[0]=deque([numssorted[0]])
        for i in range(1,len(nums)):
            if numssorted[i]-numssorted[i-1]>limit:
                currgroup+=1
            num_group[numssorted[i]]=currgroup
            if currgroup not in group_list:
                group_list[currgroup]=deque()
            group_list[currgroup].append(numssorted[i])
        for i,num in enumerate(nums):
            group=num_group[num]
            nums[i]=group_list[group].popleft()
        return nums

