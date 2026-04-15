# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #i am thinking - measure left of root and right side of root and return tehr max 
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        diameter = left_depth + right_depth

        diameterleft = self.diameterOfBinaryTree(root.left)
        diameterright= self.diameterOfBinaryTree(root.right)


        res = max( diameterright, diameterleft, diameter)
        return res




    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    






        
        