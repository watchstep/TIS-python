# 행렬 제곱
import sys;input=sys.stdin.readline

N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

# 행렬곱
def matmul(arr1, arr2):
    new_mat = [[0 for _ in range(N)] for _ in range(N)] # [[0 for _ in range(N)]]*N 하면 안됨
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_mat[i][j] += arr1[i][k] * arr2[k][j] % 1000
    return new_mat

# 분할 정복 (피보나치 참고)
def square(m, rep):
    # 제곱할 필요 없을 경우 
    if rep == 1:
        return m
    # 짝수일 경우
    if rep % 2 == 0:
        half = square(m, rep // 2) # 반 계산
        return matmul(half, half)
    # 홀수일 경우
    else:
        return matmul(m, square(m, rep - 1)) # rep -1 (홀수를 짝수로 만들기)
    
for row in square(mat, B):
    print(*[i % 1000 for i in row])
    
# https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-10830-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1