# 짝수 팰린드롬
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 2 4 6 8 ..
# 연속 두 개 같은 원소가 있으면 1개의 짝.팰
# 2개 이상부터는 뒤집었을 때 같아야 함

cnt = 0
stack = []
for i in range(N):
    if not stack or stack[-1] != arr[i]:
        stack.append(arr[i])

