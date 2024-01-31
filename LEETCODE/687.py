# 687. Longest Univalue Path

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            # 경로 내 노드 값이 모두 동일한 조건
            if node.left and (node.left.val == node.val):
                l += 1
            else:
                l = 0
            if node.right and (node.right.val == node.val):
                r += 1
            else:
                r = 0
        
            self.res = max(self.res, l + r)
            
            return max(l, r)
        
        dfs(root)
        return self.res
                               
        
        
            

        