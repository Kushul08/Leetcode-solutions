# ─────────────────────────────────────────────────
#  Problem : 0018. 4Sum
#  Difficulty : Medium
#  Runtime  : 1596 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hashset=set()
                for k in range(j+1,len(nums)):
                    bias=target-(nums[i]+nums[j]+nums[k])
                    if bias in hashset:
                        temp=[nums[i],nums[j],nums[k],bias]
                        temp.sort()
                        result.add(tuple(temp))
                    hashset.add(nums[k])
        return list(result)
        
        # nums.sort()
        # n=len(nums)
        # result=set()
        # for i in range(n-4):
        #     for j in range(i+1,n-3):
        #         k=j+1
        #         l=n-1
        #         while k<l:
        #             if nums[i]+nums[j]+nums[k]+nums[l]<target:
        #                 k+=1
        #             elif nums[i]+nums[j]+nums[k]+nums[l]>target:
        #                 l-=1
        #             else:
        #                 result.add(tuple([nums[i],nums[j],nums[k],nums[l]]))
        #                 while k<l and nums[k]==nums[k+1]:
        #                     k+=1
        #                 k+=1
        #                 while k<l and nums[l]==nums[l-1]:
        #                     l-=1
        #                 l-=1
        #         while j+1<n and nums[j]==nums[j+1]:
        #             j+=1
        #         j+=1
        #     while i+1<n and nums[i]==nums[i+1]:
        #         i+=1
        #     i+=1
        # return list(result)