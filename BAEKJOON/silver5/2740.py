# 행렬 곱셈
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# N*M, M*K
def matmul(mat1, mat2):
    # N*K
    new_mat = [[0 for _ in range(K)] for _ in range(N)]
    
    for i in range(N):
        for j in range(K):
            for k in range(M):
                new_mat[i][j] += mat1[i][k] * mat2[k][j]
    
    return new_mat

res = matmul(A, B)
for row in res:
    print(*row)