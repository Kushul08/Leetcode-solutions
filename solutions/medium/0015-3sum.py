# ─────────────────────────────────────────────────
#  Problem : 0015. 3Sum
#  Difficulty : Medium
#  Runtime  : 1861 ms
#  Memory   : 18.1 MB
#  Solved   : 2026-05-12
# ─────────────────────────────────────────────────

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # l=0
        # r=0
        # triplets=set()
        # sorted_list=sorted(nums)
        # for i in range(len(sorted_list)):
        #     for j in range(i+1,len(sorted_list)):
        #         sums=0
        #         sums=sorted_list[i]+sorted_list[j]
        #         l=j+1
        #         r=len(nums)-1
        #         while l<=r:
        #             mid=l+(r-l)//2
        #             if -(sums)==sorted_list[mid]:
        #                 triplets.add((sorted_list[i],sorted_list[j],sorted_list[mid]))
        #                 break
        #             elif -(sums)<sorted_list[mid]:
        #                 r=mid-1
        #             else:
        #                 l=mid+1
        # return list(triplets)

        
        # result=set()

        # for i in range(len(nums)):
        #     hashset=set()
        #     for j in range(i+1,len(nums)):
        #         if -(nums[i]+nums[j]) in hashset:
        #             temp=sorted([nums[i],nums[j],-(nums[i]+nums[j])])
        #             result.add(tuple(temp))
        #         hashset.add(nums[j])
        # return list(result)

        nums.sort()
        result=set()

        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            while j<k :
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    result.add(tuple([nums[i],nums[j],nums[k]]))
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    k-=1
        return list(result)