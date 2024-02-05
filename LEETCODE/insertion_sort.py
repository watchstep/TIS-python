#  Insertion Sort
# 평균 O(n^2) 최상 O(n)
# 일부 정렬되어 있을 때 효율적인 정렬 방법

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i] # 삽입할 값
        
        while i > 0 and val < arr[i - 1]: # 삽입할 값이 이전 값보다 크면 
            arr[i] = arr[i - 1] # 이전 값을 뒤로
            i -= 1
        arr[i] = val # 삽입
        

def insertion_sort_recursion(arr, n=1):
    if n == len(arr):
        return
    i = n
    while i > 0 and arr[i] < arr[i - 1]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i -= 1
    insertion_sort_recursion(arr, n + 1)