# 빙고
import sys
board = []
erase = []

for _ in range(5):
  board.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
  erase.extend(list(map(int, sys.stdin.readline().split())))

board_flatten = sum(board, [])

def get_bingo(bf):
  res = 0
  all_0 = [0]*5
  for i in range(5):
    #가로줄
    if bf[i*5:(i+1)*5] == all_0:
      res += 1
    # 세로줄
    if bf[i::5] == all_0:
      res += 1
  # 왼쪽부터 시작하는 대각선
  if bf[::6] == all_0:
    res += 1
  # 오른쪽부터 시작하는 대각선
  if bf[4::4][:5] == all_0:
    res += 1
  return res


when = 0
bingo = get_bingo(board_flatten)

for e in erase:
  if bingo >= 3:
    print(when)
    break
  idx = board_flatten.index(e)
  board_flatten[idx] = 0
  bingo = get_bingo(board_flatten)
  when += 1

############################
# 2차원 리스트 -> 1차원 리스트
sum(board, [])

# 전치행렬 만드는 법
# 1. zip 이용
board_transpose = list(zip(*board))

# 2. for 문 이용
board_transpose = []
for i in range(5):
  row = []
  for j in range(5):
    row.append(board[j][i])
  board_transpose.append(row)
