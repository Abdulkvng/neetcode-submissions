# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        #iterative bfs:

        if not root:
            return 0
        
        q = deque([root])
        currlevel = 0
        level = 0 

        while q:
            currlevel += 1
            level = max(level, currlevel)
            for i in range(len(q)):
                
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return level


                
                



        # recursive dfs - max left or right + 1
        # if not root: return 0 
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iterative dfs 
        # if not root:
        #     return 0
        # res = 0
        
        # stack = [[root, 1]]
        # while stack:
        #     node, depth = stack.pop()
        #     res = max(depth, res)
        #     if node.left:
        #         stack.append([node.left, depth + 1])
        #     if node.right:
        #         stack.append([node.right, depth + 1])

        # return res




            







        



        # iterative dfs
        # bfs 



        