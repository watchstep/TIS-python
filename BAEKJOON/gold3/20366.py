# 같이 눈사람 만들래?
import sys;input=sys.stdin.readline

N = int(input())
diameter = list(map(int, input().split()))

diameter.sort()
diff = sys.maxsize

for i in range(N): # 첫 번째 원소는 고정
    for j in range(i + 3, N): # i와 j 사이 최소 2개 이상의 원소는 있어야하므로
        start, end = i + 1, j - 1
        while start < end:
            tmp = (diameter[i] + diameter[j]) - (diameter[start] + diameter[end])
            diff = min(diff, abs(tmp))
            if tmp < 0:
                end -= 1
            else:
                start += 1
                
print(diff)