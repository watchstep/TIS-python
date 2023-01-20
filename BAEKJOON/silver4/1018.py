# 체스판 다시 칠하기
N, M = map(int, input().split())

board = []
chess_B = []

for _ in range(4):
  chess_B.append(list('BWBWBWBW'))
  chess_B.append(list('WBWBWBWB'))

chess_W = chess_B[::-1]  

for _ in range(N):
  board.append(list(input()))

temp_b_cnt = 0
temp_w_cnt = 0
temp_cnt_list = []

for i in range(N-7):
  for j in range(M-7):
    temp_b_cnt = 0
    temp_w_cnt = 0
    for v in range(i, i+8): # vertical
      for h in range(j, j+8): # horizon
        if board[v][h] != chess_B[v-i][h-j]:
            temp_b_cnt += 1
        else:
          if board[v][h] != chess_W[v-i][h-j]:
            temp_w_cnt += 1 
    if temp_b_cnt > temp_w_cnt:
      temp_cnt_list.append(temp_w_cnt)
    else:
      temp_cnt_list.append(temp_b_cnt)

print(min(temp_cnt_list))

# 다른 풀이
N, M = map(int, input().split())

board = []
cnt = []

for _ in range(N):
  board.append(input())

