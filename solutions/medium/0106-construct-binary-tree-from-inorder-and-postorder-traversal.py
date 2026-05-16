# ─────────────────────────────────────────────────
#  Problem : 0106. Construct Binary Tree from Inorder and Postorder Traversal
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 17.5 MB
#  Solved   : 2026-05-16
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inmap={}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i
        
        def build(postorder,poststart,postend,inorder,instart,inend,inmap):
            if poststart>postend or instart>inend:
                return None
            
            root=TreeNode(postorder[postend])

            inroot=inmap[postorder[postend]]
            leftremain=inroot-instart

            root.left=build(postorder,poststart,poststart+leftremain-1,
                            inorder,instart,inroot-1,inmap)
            root.right=build(postorder,poststart+leftremain,postend-1,
                            inorder,inroot+1,inend,inmap)
            return root
        return build(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,inmap)