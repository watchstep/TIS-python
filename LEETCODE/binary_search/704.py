# 704. Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            if start <= end:
                mid = (start + end) // 2
                mid_num = nums[mid]
                if target > mid_num:
                    return binary_search(mid + 1, end)
                elif mid_num > target:
                    return binary_search(start, mid - 1)
                else:
                    return mid
            else:
                return -1
        return binary_search(0, len(nums) - 1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            mid_num = nums[mid]
            
            if target > mid_num:
                start = mid + 1
            elif mid_num > target:
                end = mid - 1
            else:
                return mid
        return -1
    
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        idx = bisect.bisect_left(nums, target)
        
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            return -1