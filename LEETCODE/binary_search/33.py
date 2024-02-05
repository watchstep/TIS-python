# 33. Search in Rotated Sorted Array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        # pivot k 찾기
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            mid_num = nums[mid]
            if mid_num > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        pivot = start
        
        # pivot 기준으로 이진 검색
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_pivot = (mid + pivot) % len(nums)
			# mid에 pivot만큼 이동하고, 배열의 길이 초과할 경우
			# 모듈로 연산으로 회전될 수 있도록
            mid_pivot_nums = nums[mid_pivot]
            
            if target > mid_pivot_nums:
                start = mid + 1
            elif mid_pivot_nums > target:
                end = mid - 1
            else:
                return mid_pivot
        return -1
    
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid -1
        return -1