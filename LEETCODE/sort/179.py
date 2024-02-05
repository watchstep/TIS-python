# 179. Largest Number

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def to_swap(n1, n2):
            return str(n1) + str(n2) < str(n2) + str(n1)
    
        for i in range(1, len(nums)):
            while (i > 0) and (to_swap(nums[i - 1], nums[i])): # 삽입할 값이 이전 값보다 크면
                nums[i], nums[i - 1] = nums[i - 1], nums[i] # swap
                i -= 1
        return str(int(''.join(map(str, nums))))

# 기본 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i] # 삽입할 값
        
        while i > 0 and val < arr[i - 1]: # 삽입할 값이 이전 값보다 크면 
            arr[i] = arr[i - 1] # 이전 값을 뒤로
            i -= 1
        arr[i] = val # 삽입
        