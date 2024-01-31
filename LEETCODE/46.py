# 46. Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        prev_elems = []
        
        def dfs(elems):
            # leaf node []일 때 결과 추가
            if not elems:
                res.append(prev_elems[:])
            
            # 순열 생성 재귀 호출
            for e in elems:
                next_elems = elems[:]
                next_elems.remove(e)
                
                prev_elems.append(e)
                dfs(next_elems)
                prev_elems.pop()
        
        dfs(nums)
        return res
    
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(map(list, permutations(nums)))