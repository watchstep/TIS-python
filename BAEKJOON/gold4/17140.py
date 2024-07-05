# 이차원 배열과 연산
import sys;input=sys.stdin.readline
from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def rc_cal(lst):
    lst = [i for i in lst if i != 0]
    count_dic = Counter(lst)
    sorted_dic = sorted(count_dic.items(), key=lambda x: (x[1], x[0]))
    return list(sum(sorted_dic, ())) # flatten

def rc_sort(a):
    sorted_arr = []
    row = len(a)
    col = len(a[0])
    max_len = 0
    
    if row >= col:
        for i in range(row):
            sorted_row = rc_cal(a[i])
            sorted_arr.append(sorted_row)
            max_len = max(max_len, len(sorted_row))
        padded_arr = [i + [0]*(max_len - len(i)) for i in sorted_arr]
    else:
        converted_arr = list(zip(*a))
        for i in range(col):
            sorted_col = rc_cal(converted_arr[i])
            sorted_arr.append(sorted_col)
            max_len = max(max_len, len(sorted_col))
        padded_arr = [i + [0]*(max_len - len(i)) for i in sorted_arr]
        padded_arr = list(zip(*padded_arr))
    
    row = len(padded_arr)
    col = len(padded_arr[0])
    if row > 100:
        padded_arr = padded_arr[:101]
    if col > 100:
        padded_arr = [i[:101] for i in padded_arr]
        
    return padded_arr
 

for t in range(101):
    row = len(arr)
    col = len(arr[0])
    if row >= r and col >= c and arr[r - 1][c - 1] == k:
        print(t)
        break
    arr = rc_sort(arr)
else:   
    print(-1)