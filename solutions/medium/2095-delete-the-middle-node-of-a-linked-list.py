# ─────────────────────────────────────────────────
#  Problem : 2095. Delete the Middle Node of a Linked List
#  Difficulty : Medium
#  Runtime  : 79 ms
#  Memory   : 91.7 MB
#  Solved   : 2026-06-15
# ─────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head