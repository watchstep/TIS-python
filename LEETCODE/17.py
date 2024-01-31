# 17. Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from itertools import product
        letters  = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        comp = []
        res = []
        def dfs(digits, x):
            if digits[x] == '':
                return comp
            comp.append(letters[digits[x]])
            digits = digits[x+1:]
                
        for i in range(len(digits)):
            dfs(digits, i)

        for i in product(*comp):
            res.append(''.join(i))
            
        if not comp:
            return []
        return res
            
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
                
            for i in range(index, len(digits)): # digits 자릿수만큼 반복
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        if not digits:
            return []
        
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        dfs(0, '')
        
        return result            