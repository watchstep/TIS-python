# 01타일
import sys
input = sys.stdin.readline
N = int(input())

seq = [0]*1000001

seq[1] = 1
seq[2] = 2

for i in range(3, N+1):
  seq[i] = (seq[i-1] + seq[i-2])%15746
print(seq[N])

# 메모리 초과
print(seq[N]%15746)
# 결괏값에 나누면 수시로 연산해서 메모리 초과 발생
# 규칙을 찾아본 결과
'''
N=1 : 1
N=2 : 2
N=3 : 3
N=4 : 5
N=5 : 8
'''