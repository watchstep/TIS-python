# 색종이
N = int(input())

# 도화지를 0으로만 이루어진 100*100 바둑판으로 설정
# [[0, 0, ~, 0], [0, 0, ~, 0], ~ [0, 0, ~, 0]]
drawing_paper = [[0]*100 for _ in range(100)]

for _ in range(N):
  left, bottom = map(int, input().split())
  
  for i in range(left, left+10): # 가로
    for j in range(bottom, bottom+10): # 세로
      drawing_paper[i][j] = 1 # 해당 칸을 0에서 1로 변경
      
cnt = 0

for i in range(100):
  cnt += drawing_paper[i].count(1) # 1 카운트
  
print(cnt)