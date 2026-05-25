# ─────────────────────────────────────────────────
#  Problem : 0173. Binary Search Tree Iterator
#  Difficulty : Medium
#  Runtime  : 11 ms
#  Memory   : 20.8 MB
#  Solved   : 2026-05-25
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.nums=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.nums.append(root.val)
            inorder(root.right)
        inorder(root)
        self.i=0
    def next(self):
        """
        :rtype: int
        """
        if self.i<len(self.nums):
            val=self.nums[self.i]
            self.i+=1
            return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i<len(self.nums):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()