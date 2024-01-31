# 215. Kth Largest Element in an Array

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from heapq import heappush, heappop
        
        heap = []
        for n in nums:
            heappush(heap, -n) # 파이썬 heapq 모듈 최소 힙만 지원 -> 음수로 저장
        
        for _ in range(k - 1): # k-1번째까지 추출하고
            heappop(heap)
        
        return - heappop(heap) # k번째 큰 수 반환


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heapify, heappop
        
        heapify(nums) # 힙으로 변환 (유의해야할 것: 하나라도 값 추가하면 힙 특성 깨짐)
        n = len(nums)
        for _ in range(n - k):
            heappop(nums)
        return heappop(nums)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import nlargest
        
        return nlargest(k, nums)[-1]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]