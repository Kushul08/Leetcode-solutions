# ─────────────────────────────────────────────────
#  Problem : 2130. Maximum Twin Sum of a Linked List
#  Difficulty : Medium
#  Runtime  : 358 ms
#  Memory   : 93.4 MB
#  Solved   : 2026-06-14
# ─────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        max_sum=0
        for i,j in zip(range(len(nums)),range(len(nums)-1,-1,-1)):
            if i>j:
                break
            max_sum=max(max_sum,nums[i]+nums[j])
        return max_sum