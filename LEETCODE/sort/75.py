# 75. Sort Colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def insertion_sort():
            for i in range(1, len(nums)):
                val = nums[i]
                while (i > 0) and (val < nums[i - 1]):
                    nums[i] = nums[i - 1]
                    i -= 1
                nums[i] = val
                
        insertion_sort()
        return nums

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) # lo, mid, hi
        
        while w < b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 2:
                b -= 1
                nums[w], nums[b] = nums[b], nums[w]
            else:
                w += 1

def dutch_flag(arr):
    lo, hi, mid = 0, len(arr), 0
    
    while mid < hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr
                