# 336. Palindrome Pairs


# 시간 초과
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    pass
                else:
                    s = words[i] + words[j]
                    if s == s[::-1]:
                        res.append([i, j])
        return res
# 시간 초과
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word):
            return word == word[::-1]
        
        res = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(w1 + w2):
                    res.append([i, j])
        return res