# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return -1 # 존재하지 않는 node -1
            
            l = dfs(root.left) 
            r = dfs(root.right)
            
            self.diameter = max(self.diameter, l + r + 2)
            return max(l, r) + 1 # 상태값
        
        dfs(root)
        return self.diameter
    
class Solution(object):
    diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            
            self.diameter = max(self.diameter, l + r - 2)
            
            return max(l, r)
        
        dfs(root)
        return self.diameter
            
            