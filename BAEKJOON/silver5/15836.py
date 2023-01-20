# Matrix Multiplication Calculator
def get_input():
  M, N, P, Q = map(int, input().split())
  
  A = []
  B = []
  for _ in range(M):
    A.append(list(map(int, input().split())))
    
  for _ in range(P):
    B.append(list(map(int, input().split())))
    
  return M, N, P, Q, A, B

def matmul(M, Q, N, A, B):
  res = []
  for m in range(M):
    res.append([0]*Q) # 먼저, return해야할 빈 행렬 생성
  
  s = 0
  for m in range(M):
    for q in range(Q):
      for n in range(N): # 중간에 있는 것이 움직이면서 matmul
        s += A[m][n] * B[n][q]
      res[m][q] = s
      s = 0
  return res

case_num = 0
M, N, P, Q, A, B = get_input()

while M != 0 and N != 0 and P !=0 and Q !=0:
  if N == P:
    res = matmul(M, Q, N, A, B)
    print(f"Case #{case_num+1}:")
    for i in range(M):
      print('|', ' '.join([str(j) for j in res[i]]), '|')
    M, N, P, Q, A, B = get_input()
  else:
    print(f'Case #{case_num+1}:')
    print("undefined")
    M, N, P, Q, A, B = get_input()
  case_num += 1
  


# +) transpose
A_transpose = []

for n in range(N):
  A_transpose.append([0]*M)
  
for m in range(M):
  for n in range(N):
    A_transpose[n][m] = A[m][n]

A_transpose