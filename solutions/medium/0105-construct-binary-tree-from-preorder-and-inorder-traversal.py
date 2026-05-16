# ─────────────────────────────────────────────────
#  Problem : 0105. Construct Binary Tree from Preorder and Inorder Traversal
#  Difficulty : Medium
#  Runtime  : 12 ms
#  Memory   : 17.3 MB
#  Solved   : 2026-05-16
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inmap={}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i

        def build(preorder,prestart,preend,inorder,instart,inend,inmap):
            if prestart>preend or instart>inend:
                return None
            
            root=TreeNode(preorder[prestart])

            inroot=inmap[preorder[prestart]]
            leftremain=inroot-instart

            root.left=build(preorder,prestart+1,prestart+leftremain,
                            inorder,instart,inroot-1,inmap)
            root.right=build(preorder,prestart+leftremain+1,preend,
                            inorder,inroot+1,inend,inmap)
            return root
        return build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inmap)
