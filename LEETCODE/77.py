# 77. Combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(elems, start, k):
            if not k:
                res.append(elems[:])
            
            for i in range(start, n + 1):
                elems.append(i)
                dfs(elems, i + 1, k - 1)
                elems.pop()
        dfs([], 1, k)
        return res
        