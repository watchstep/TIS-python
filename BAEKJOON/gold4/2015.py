# 수들의 합 4
import sys;input=sys.stdin.readline

N, K =  map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0

for i in arr:
    tmp += i
    prefix_sum.append(tmp)
    
cnt = 0
for i in range(N):
    for j in range(i, N):
        psum = arr[j] - arr[i]
        if psum == K:
            cnt += 1
        
print(cnt)

import sys;input=sys.stdin.readline

N, K =  map(int, input().split())
arr = list(map(int, input().split()))
sum_dict = {0: 1}  
val = 0 
cnt = 0  
for i in arr:
    val += i
    if val - K in sum_dict.keys():  
        cnt += sum_dict[val - K]  
    if val in sum_dict.keys():
        sum_dict[val] += 1
    else:
        sum_dict[val] = 1
print(cnt)