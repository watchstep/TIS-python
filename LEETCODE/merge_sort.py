# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 # divide 
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left) # conquer
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right): # merge
    res = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        
    res += left[i:]
    res += right[j:]
    
    return res

# left = [2, 24, 26] right = [16, 25, 31, 32]
# left와 right의 첫째 원소끼리 비교해 작은 원소를 res에 넣기. => res = [2]
# left의 둘째 원소와 right의 첫째 원소를 비교해 작은 원소를 res에 넣기 => res = [2, 16]
# 모든 원소가 res에 들어갈 때까지 반복 => [2, 16, 24, 25, 26]
# 남은 원소를 순서대로 res에 넣기 => [2, 16, 24, 25, 26, 31, 32]
